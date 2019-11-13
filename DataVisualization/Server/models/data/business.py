# -*- coding: utf-8 -*-
import json
from ...models.dao import redisDao
import threading
from ...librarys import env

_businessInstance = None


class Business():

    _instance_lock = threading.Lock()
    redis = redisDao.connect()
    data = {}

    def __init__(self):
        pass

    def radius(self, longitude, latitude, radius, unit='mi'):
        result = []
        geoList = self.redis.georadius('afrss_business', longitude=longitude, latitude=latitude, radius=radius,
                                       unit=unit, withdist=True, withcoord=False, withhash=False, count=None,
                                       sort='ASC', store=None, store_dist=None)
        for item in geoList:
            result.append({
                'business_id': item[0].decode('utf-8'),
                'distance': item[1],
            })
        return result

    def getItem(self, id):
        print(id)
        if id in self.data:
            return self.data[id], True
        return {}, False

    def setItem(self, id, item):
        self.data[id] = item
        return True

    def getItems(self, ids):
        items = []
        for id in ids:
            item, exists = self.getItem(id)
            if not exists:
                continue
            items.append(item)
        return items

    def setItems(self, items):
        for id, item in items:
            self.setItem(id, item)
        return True

    def add(self, *values):
        return self.redis.geoadd('afrss_business', *values)

    def load(self, loadData=False, loadGEO=False):
        dataPath = env.getDataPath()
        fp = open(dataPath + 'yelp_dataset/business.json',
                  'r', encoding='utf8')
        fp.readline()
        count = 0
        values = []
        limit = 1000
        total = 0
        while True:
            line = fp.readline()
            if loadGEO and (count >= limit or (not line and count > 0)):
                total += self.add(*values)
                count = 0
                values = []
            if not line:
                break
            data = json.loads(line)
            if data['state'] == 'AZ' and data['city'] == 'Phoenix':
                # Insert memory
                if loadData:
                    self.setItem(data['business_id'], data)
                # Insert redis geo data
                if loadGEO:
                    count += 1
                    values.append(data['longitude'])
                    values.append(data['latitude'])
                    values.append(data['business_id'])
        fp.close()
        return total

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with cls._instance_lock:
                if not hasattr(cls, '_instance'):
                    cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

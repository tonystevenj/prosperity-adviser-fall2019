# -*- coding: utf-8 -*-
import json
import csv
from ...models.dao import redisDao
import threading
from ...librarys import env

_businessInstance = None


class Park():

    _instance_lock = threading.Lock()
    redis = redisDao.connect()
    data = {}

    def __init__(self):
        pass

    def radius(self, longitude, latitude, radius, unit='mi'):
        result = []
        geoList = self.redis.georadius('afrss_park', longitude=longitude, latitude=latitude, radius=radius,
                                       unit=unit, withdist=True, withcoord=False, withhash=False, count=None,
                                       sort='ASC', store=None, store_dist=None)
        for item in geoList:
            result.append({
                'name': item[0].decode('utf-8'),
                'distance': item[1],
            })
        print(result)
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
        return self.redis.geoadd('afrss_park', *values)

    def load(self, loadData=False, loadGEO=False):
        dataPath = env.getDataPath()
        fp = open(dataPath + 'parks.csv', 'r', encoding='utf8')
        fpcsv = csv.reader(fp)
        next(fpcsv)
        count = 0
        values = []
        limit = 1000
        total = 0
        for line in fpcsv:
            if loadGEO and (count >= limit):
                total += self.add(*values)
                count = 0
                values = []
            # Insert memory
            if loadData:
                self.setItem(line[2], {
                    'longitude': line[0],
                    'latitude': line[1],
                    'name': line[2],
                    'adress': line[3],
                    'zipcode': line[6],
                    'url': line[7],
                })
            # Insert redis geo data
            if loadGEO:
                count += 1
                values.append(line[0])
                values.append(line[1])
                values.append(line[2])
        if count > 0:
            total += self.add(*values)
        fp.close()
        return total

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with cls._instance_lock:
                if not hasattr(cls, '_instance'):
                    cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

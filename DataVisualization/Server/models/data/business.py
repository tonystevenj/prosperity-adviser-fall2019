# -*- coding: utf-8 -*-
import json
import csv
from ...librarys import env
from . import base


class Business():
    """
    商家数据导入
    """

    def load(self):
        """ 数据导入
        Return: dict, dict
                两个返回的key都为数据唯一标识，比如business_id，
                第一个返回值为商家详细信息，存在进程内存中，使用business_id查找
                第二个返回值为地理位置信息，存在redis中，值为dict{longitude, latitude}
        """
        dataPath = env.getDataPath()
        fp = open(dataPath + 'yelp_dataset/business_Phoenix_Restaurant_processed2.csv',
                  'r', encoding='utf8')
        fpcsv = csv.reader(fp)
        titles = next(fpcsv)
        items = {}
        geoItems = {}
        for line in fpcsv:
            tmpItem = {}
            for i in range(len(line)):
                if line[i] == 'TRUE':
                    tmpItem[titles[i]] = True
                elif line[i] == 'FALSE':
                    tmpItem[titles[i]] = False
                else:
                    tmpItem[titles[i]] = line[i]
            items[tmpItem['business_id']] = tmpItem
            geoItems[tmpItem['business_id']] = {
                'longitude': tmpItem['longitude'],
                'latitude': tmpItem['latitude'],
            }
        fp.close()
        return items, geoItems

    def loadOriginal(self):
        """ 数据导入
        Return: dict, dict
                两个返回的key都为数据唯一标识，比如business_id，
                第一个返回值为商家详细信息，存在进程内存中，使用business_id查找
                第二个返回值为地理位置信息，存在redis中，值为dict{longitude, latitude}
        """
        dataPath = env.getDataPath()
        fp = open(dataPath + 'yelp_dataset/business.json',
                  'r', encoding='utf8')
        items = {}
        geoItems = {}
        for line in fp:
            data = json.loads(line)
            if data['state'] == 'AZ' and data['city'] == 'Phoenix':
                # 商家数据
                items[data['business_id']] = data
                # 经纬度数据
                geoItems[data['business_id']] = {
                    'longitude': data['longitude'],
                    'latitude': data['latitude']
                }
        fp.close()
        return items, geoItems


# 最后需要调用base.regObj注册数据处理对象，
# 然后在同级__init.py中import执行这个文件
base.regObj(Business())

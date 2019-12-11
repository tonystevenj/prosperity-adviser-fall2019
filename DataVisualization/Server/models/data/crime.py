# -*- coding: utf-8 -*-
import json
import csv
from ...librarys import env
from . import base


class Crime():
    """
    犯罪数据
    """

    def load(self):
        """ 数据导入
        Return: dict, dict
                两个返回的key都为数据唯一标识，比如business_id，
                第一个返回值为商家详细信息，存在进程内存中，使用business_id查找
                第二个返回值为地理位置信息，存在redis中，值为dict{longitude, latitude}
        """
        dataPath = env.getDataPath()
        fp = open(dataPath + 'crime-data_crime-data_crimestat.csv',
                  'r', encoding='utf8')
        fpcsv = csv.reader(fp)
        titles = next(fpcsv)
        items = {}
        geoItems = {}
        for line in fpcsv:
            tmpItem = {}
            for i in range(len(line)):
                tmpItem[titles[i].lower()] = line[i]
            if tmpItem['zip'] not in items:
                items[tmpItem['zip']] = {}
            if tmpItem['ucr crime category'] not in items[tmpItem['zip']]:
                items[tmpItem['zip']][tmpItem['ucr crime category']] = []
            items[tmpItem['zip']][tmpItem['ucr crime category']].append(tmpItem)
        return items, geoItems


# 最后需要调用base.regObj注册数据处理对象，
# 然后在同级__init.py中import执行这个文件
base.regObj(Crime())

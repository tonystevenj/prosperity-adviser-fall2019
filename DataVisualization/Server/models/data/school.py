# -*- coding: utf-8 -*-
import json
import csv
from ...librarys import env
from . import base


class School():
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
        fp = open(dataPath + 'Phoenix School Enrollment Data_with_Location_Data.csv',
                  'r', encoding='ISO-8859-1')
        fpcsv = csv.reader(fp)
        titles = next(fpcsv)
        items = {}
        geoItems = {}
        for line in fpcsv:
            tmpItem = {}
            for i in range(len(line)):
                tmpItem[titles[i].lower()] = line[i]
            items[tmpItem['school name']] = tmpItem
            geoItems[tmpItem['school name']] = {
                'longitude': tmpItem['longitude'],
                'latitude': tmpItem['latitude'],
            }
        fp.close()
        return items, geoItems


# 最后需要调用base.regObj注册数据处理对象，
# 然后在同级__init.py中import执行这个文件
base.regObj(School())

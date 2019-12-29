# -*- coding: utf-8 -*-
import csv
from ...librarys import env
from . import base


class Park():
    """
    公园数据
    """

    def load(self):
        dataPath = env.getDataPath()
        fp = open(dataPath + 'parks.csv', 'r', encoding='utf8')
        fpcsv = csv.reader(fp)
        next(fpcsv)
        items = {}
        geoItems = {}
        for line in fpcsv:
            # 商家数据
            items[line[2]] = {
                'longitude': line[0],
                'latitude': line[1],
                'name': line[2],
                'adress': line[3],
                'zipcode': line[6],
                'url': line[7],
            }
            # 经纬度数据
            geoItems[line[2]] = {
                'longitude': line[0],
                'latitude': line[1],
            }
        fp.close()
        return items, geoItems


base.regObj(Park())

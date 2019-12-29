# -*- coding: utf-8 -*-
import csv
from ...librarys import env
from . import base


class PopAge():
    """
    人口年龄分布
    """

    def load(self):
        dataPath = env.getDataPath()
        fp = open(dataPath + 'Phoenix_Age_Distribution_Data.csv', 'r', encoding='utf8')
        fpcsv = csv.reader(fp)
        titles = next(fpcsv)
        items = {}
        geoItems = {}
        for line in fpcsv:
            tmpItem = {}
            for i in range(len(line)):
                tmpItem[titles[i].lower()] = line[i]
            items[tmpItem['zipcode']] = tmpItem
        fp.close()
        return items, geoItems


base.regObj(PopAge())

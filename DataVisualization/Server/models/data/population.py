# -*- coding: utf-8 -*-
import csv
from ...librarys import env
from . import base


class Population():
    """
    人口数据
    """

    def load(self):
        dataPath = env.getDataPath()
        fp = open(dataPath + 'population.csv', 'r', encoding='utf8')
        fpcsv = csv.reader(fp)
        next(fpcsv)
        items = {}
        geoItems = {}
        for line in fpcsv:
            zipcode = line[0]
            valueType = line[1]
            value = line[2]
            if zipcode not in items:
                items[zipcode] = {}
            value = value.replace(',', '')
            items[zipcode][valueType] = float(value)
        fp.close()
        return items, geoItems


base.regObj(Population())

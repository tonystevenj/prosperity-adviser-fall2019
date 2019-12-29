# -*- coding: utf-8 -*-
import csv
import unicodedata
from ...librarys import env
from . import base


class PopRace():
    """
    Population race
    """

    def load(self):
        dataPath = env.getDataPath()
        fp = open(
            dataPath + 'pop-sdc-azzcta-service-area-statistics.csv', 'r', encoding='utf8')
        fpcsv = csv.reader(fp)
        titles = next(fpcsv)
        items = {}
        geoItems = {}
        for line in fpcsv:
            tmpItem = {}
            for i in range(len(line)):
                tmpItem[titles[i].lower()] = line[i]
            zipcode = tmpItem['geography'][6:11]
            if self.is_number(zipcode):
                items[zipcode] = tmpItem
        fp.close()
        return items, geoItems

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False


base.regObj(PopRace())

# -*- coding: utf-8 -*-
import csv
from ...librarys import env


class Business():

    def __init__(self):
        pass

    def load(self):
        dataPath = env.getDataPath()
        with open(dataPath + 'finaloutputs0.csv', "r", encoding='utf8') as csvfile:
            reader = csv.reader(csvfile)
            for line in reader:
                print(line)


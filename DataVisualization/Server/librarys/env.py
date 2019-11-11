# -*- coding: utf-8 -*-
import os
import sys


class Env():

    basePath = ''
    dataPath = ''

    def __init__(self):
        self.basePath = os.path.abspath(os.path.dirname(sys.argv[0])+os.path.sep+".") + '/'
        self.dataPath = self.basePath + 'data/'

    def getBasePath(self):
        return self.basePath

    def getDataPath(self):
        return self.dataPath

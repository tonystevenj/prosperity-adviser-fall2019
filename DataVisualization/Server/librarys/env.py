# -*- coding: utf-8 -*-
import os
import sys


class Env():

    basePath = ''

    def __init__(self):
        self.basePath = os.path.abspath(
            os.path.dirname(sys.argv[0])+os.path.sep+".") + '/'

    def getBasePath(self):
        return self.basePath

    def getDataPath(self):
        return self.basePath + '/data/'

    def getConfigPath(self):
        return self.basePath + '/config/'

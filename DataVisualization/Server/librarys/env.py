# -*- coding: utf-8 -*-
import os
import sys


class Env():

    basePath = ''

    def __init__(self):
        self.basePath = os.path.abspath(
            os.path.dirname(sys.argv[0])+os.path.sep+".") + '/'

    def getProjectPath(self):
        return self.basePath
        # return os.path.abspath(os.path.join(os.getcwd(), ".."))

    def getBasePath(self):
        return self.basePath

    def getDataPath(self):
        return self.basePath + '/data/'

    def getConfigPath(self):
        return self.basePath + '/config/'

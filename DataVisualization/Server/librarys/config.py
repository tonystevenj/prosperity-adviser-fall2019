# -*- coding: utf-8 -*-
import toml
from ..librarys import env


def load(path):
    configPath = env.getConfigPath()
    return toml.load(configPath + path)

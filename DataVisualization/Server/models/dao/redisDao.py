# -*- coding: utf-8 -*-
import redis
import toml
from ...librarys import config

redisDao = None


def connect():
    global redisDao
    if redisDao == None:
        conf = config.load('redis.toml')
        redisDao = redis.Redis(host=conf['host'], port=conf['port'], password=conf['password'])
    return redisDao

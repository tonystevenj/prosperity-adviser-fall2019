# -*- coding: utf-8 -*-
import redis

redisDao = None


def connect():
    global redisDao
    if redisDao == None:
        redisDao = redis.Redis(host='sx.hopeness.net', port=6378)
    return redisDao

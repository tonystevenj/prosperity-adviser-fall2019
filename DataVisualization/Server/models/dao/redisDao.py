# -*- coding: utf-8 -*-
import redis

redisDao = None


def connect():
    global redisDao
    if redisDao == None:
        redisDao = redis.Redis(host='127.0.0.1', port=6379)
    return redisDao

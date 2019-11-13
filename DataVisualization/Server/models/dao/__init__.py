# -*- coding: utf-8 -*-
from . import redisDao


redis = redisDao.connect()
__all__ = ['redis']

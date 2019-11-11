# -*- coding: utf-8 -*-
from . import business

businessObj = business.Business()
businessObj.load()

__all__ = ['business']

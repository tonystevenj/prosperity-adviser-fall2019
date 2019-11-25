# -*- coding: utf-8 -*-
# flake8: noqa
from qiniu import Auth
from qiniu import BucketManager
access_key = 'fWDyTnj2bvRZNmlsZR9kLdfMtjswThPFGWXjbdoR'
secret_key = 'ni4xK_1xCPGchgnr0HkDQi0B50xY3a8opyx3qHf5'
#初始化Auth状态
q = Auth(access_key, secret_key)
#初始化BucketManager
bucket = BucketManager(q)
#你要测试的空间， 并且这个key在你空间中存在
bucket_name = 'afrss'
key = 'review_Phoenix.csv'
key2 = 'business22.json'
key3 = 'filesInfo.json'

#获取文件的状态信息
ret, info = bucket.stat(bucket_name, key)
# ret2, info2 = bucket.stat(bucket_name, key2)
ret, info = bucket.delete(bucket_name, key3)
ret2, info2 = bucket.stat(bucket_name, key3)
print(ret)
print(info)
print(ret2)
print(type(ret2))
print(str(ret2)=="None")
print(info2)
assert 'hash' in ret
# 删除文件
#删除bucket_name 中的文件 key
# from librarys import env
# import json
# proPath = env.getProjectPath()
# with open("F:\\pycharm-workspace\\Project_YelpDataSet\\DataVisualization\\Server/data/filesInfo.json", 'r') as load_f:
#     load_dict = json.load(load_f)
# print(load_dict)
# for i in range(len(load_dict)):
#     filename = load_dict[i][1]
#     ret, info = bucket.delete(bucket_name, filename)
#     print(info)
#     assert ret == {}
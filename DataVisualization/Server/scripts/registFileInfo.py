import os
from ..librarys import env
import json


def active(writeToJson):
    path = env.getProjectPath()
    print(path)
    filesInfo = []  # two dimensional, every row with two column, first is path, second is file name
    def core(pathinner):
        pathall = path+pathinner
        files = os.listdir(pathall)
        for file in files:
            if os.path.isdir(pathall + "/" + file):
                core(pathinner + "/" + file)
            else:
                if file!="filesInfo.json":
                    filesInfo.append([pathinner, file])

    core("data")
    print(filesInfo)
    if writeToJson:
        file_name = path+'/data/filesInfo.json'  # 通过扩展名指定文件存储的数据为json格式
        with open(file_name, 'w') as file_object:
            json.dump(filesInfo, file_object)
        filesInfo.append(["data","filesInfo.json"])
    return filesInfo

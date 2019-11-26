import os
from ..librarys import env
import json


def active(writeToJson):
    path = env.getProjectPath() + "data"
    filesInfo = []  # two dimensional, every row with two column, first is path, second is file name
    def core(path):
        files = os.listdir(path)
        for file in files:
            if os.path.isdir(path + "/" + file):
                core(path + "/" + file)
            else:
                if file!="filesInfo.json":
                    filesInfo.append([path, file])

    core(path)
    # print(filesInfo)
    if writeToJson:
        file_name = path+'/filesInfo.json'  # 通过扩展名指定文件存储的数据为json格式
        with open(file_name, 'w') as file_object:
            json.dump(filesInfo, file_object)
        filesInfo.append([path,"filesInfo.json"])
    return filesInfo

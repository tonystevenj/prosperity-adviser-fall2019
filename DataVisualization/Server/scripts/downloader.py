import wget
from ..librarys import env
import json
import os
import datetime as d
def active():
    proPath = env.getProjectPath()
    randomNum = d.datetime.now().strftime("%Y%m%d%H%M%S")

    if os.path.exists(proPath + '/data' + "/" + "filesInfo.json"):
        os.remove(proPath + '/data' + "/" + "filesInfo.json")
    wget.download("http://afrsscdn.hopeness.net/filesInfo.json?"+randomNum, out=proPath + '/data')
    # print("哈哈")
    print("Download filesInfo.json succeed")
    with open(proPath + '/data'+"/filesInfo.json", 'r') as load_f:
        load_dict = json.load(load_f)
    # print("Downloading files")
    for i in range(len(load_dict)):
        filename = load_dict[i][1]
        filepath = load_dict[i][0]
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        if not os.path.exists(filepath+"/"+filename):
            wget.download(f"http://afrsscdn.hopeness.net/{filename}", out=filepath)
            print(f"Downloads {filename} succeed")
        else:
            print(f"{filename} exists, skip downloading")
# action()

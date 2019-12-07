import math
import numpy as np
import random
import pandas as pd
import matplotlib.pyplot  as plt


def show_fig():
    dataSet = loadDataSet()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(dataSet[:, 0], dataSet[:, 1])
    plt.show()


def calcuDistance(vec1, vec2):
    # 计算向量1与向量2之间的欧式距离
    return np.sqrt(np.sum(np.square(vec1 - vec2)))  # 注意这里的减号


def loadDataSet():
    data = pd.read_csv("Data/parks.csv").to_numpy(str).T[0:2].T
    data_convert = data.astype(float)
    # print(len(data_convert))
    # print(data_convert[0])
    # print(type(data_convert))
    return data_convert


def initCentroids(dataSet, k):
    # 从数据集中随机选取k个数据返回
    dataSet = list(dataSet)
    # print(len(dataSet))
    return random.sample(dataSet, k)


def minDistance(dataSet, centroidList):
    # 对每个属于dataSet的item， 计算item与centroidList中k个质心的距离，找出距离最小的，并将item加入相应的簇类中
    clusterDict = dict()  # dict保存簇类结果
    k = len(centroidList)
    for item in dataSet:
        vec1 = item
        flag = -1
        minDis = float("inf")  # 初始化为最大值
        for i in range(k):
            vec2 = centroidList[i]
            distance = calcuDistance(vec1, vec2)  # error
            if distance < minDis:
                minDis = distance
                flag = i  # 循环结束时， flag保存与当前item最近的蔟标记
        if flag not in clusterDict.keys():
            clusterDict.setdefault(flag, [])
        clusterDict[flag].append(item)  # 加入相应的类别中
    return clusterDict  # 不同的类别


def getCentroids(clusterDict):
    # 重新计算k个质心
    centroidList = []
    for key in clusterDict.keys():
        centroid = np.mean(clusterDict[key], axis=0)
        centroidList.append(centroid)
    return centroidList  # 得到新的质心


def getVar(centroidList, clusterDict):
    # 计算各蔟集合间的均方误差
    # 将蔟类中各个向量与质心的距离累加求和
    sum = 0.0
    for key in clusterDict.keys():
        vec1 = centroidList[key]
        distance = 0.0
        for item in clusterDict[key]:
            vec2 = item
            distance += calcuDistance(vec1, vec2)
        sum += distance
    return sum


def showCluster(centroidList, clusterDict):
    # 展示聚类结果
    colorMark = ['or', 'ob', 'og', 'ok', 'oy', 'ow', 'oc']  # 不同簇类标记，o表示圆形，另一个表示颜色
    centroidMark = ['dr', 'db', 'dg', 'dk', 'dy', 'dw', 'dc']

    for key in clusterDict.keys():
        plt.plot(centroidList[key][0], centroidList[key][1], centroidMark[key], markersize=12)  # 质心点
        for item in clusterDict[key]:
            plt.plot(item[0], item[1], colorMark[key])

    plt.show()


def test_k_means():
    dataSet = loadDataSet()
    centroidList = initCentroids(dataSet, 7)
    clusterDict = minDistance(dataSet, centroidList)
    newVar = getVar(centroidList, clusterDict)
    oldVar = 1  # 当两次聚类的误差小于某个值是，说明质心基本确定。

    times = 2
    while abs(newVar - oldVar) >= 0.00001:
        centroidList = getCentroids(clusterDict)
        clusterDict = minDistance(dataSet, centroidList)
        oldVar = newVar
        newVar = getVar(centroidList, clusterDict)
        times += 1
        # showCluster(centroidList, clusterDict)
    showCluster(centroidList, clusterDict)
    # print("各类长度:")
    # for key in clusterDict.keys():
    #     print(len(clusterDict[key]))
    #     print(clusterDict[key])

    # 改变字典储存方式:
    clusterList = []
    for key in clusterDict.keys():
        clusterList.append(clusterDict[key])
    return clusterList


def JarvisMarch(S):
    S = np.array(S)

    def angle(u, v):
        x = v[0] - u[0]
        y = v[1] - u[1]
        if y < 0:
            class23 = True
        else:
            class23 = False
        if x < 0 and y > 0:
            class4 = True
        else:
            class4 = False
        if y == 0:
            if x == 0:
                return 361
            elif x > 0:
                return 90
            elif x < 0:
                return 270
        out = math.atan(x / y) / math.pi * 180
        if class23:
            out += 180
        if class4:
            out += 360
        return out

    leftmost = 0
    for i in range(len(S)):
        node = S[i]
        if S[leftmost][0] > node[0]:
            leftmost = i
    convexHull = []

    nownode = leftmost
    nowDegree = 0
    while True:
        convexHull.append(nownode)
        nextnode = None
        minnextDegree = None
        first = True
        for i in range(len(S)):
            nextDegree = angle(S[nownode], S[i])
            plusDegree = nextDegree - nowDegree

            if plusDegree < 0:
                continue
            if first == True:
                minplusDegree = plusDegree
                first = False
            if plusDegree <= minplusDegree:
                minplusDegree = plusDegree
                minnextDegree = nextDegree
                nextnode = i
        if nextnode == leftmost:
            break
        nownode = nextnode
        nowDegree = minnextDegree
    return convexHull


def destance(u, v):
    # 0是经度
    x = (v[0] - u[0]) * (2 * math.pi * 6371 / 360) * 0.621371 * math.cos((v[1] + u[1]) / 2)
    y = (v[1] - u[1]) * (2 * math.pi * 6371 / 360) * 0.621371
    return math.sqrt(pow(x, 2) + pow(y, 2))


def calculateDensity(data_2dPoints):
    convexID = JarvisMarch(data_2dPoints)
    # print("环边输出：", convexID)
    # 计算最长两点间最长距离：
    longest = 0
    p1 = 0
    p2 = 0
    for i in range(len(convexID)):
        convex1 = data_2dPoints[convexID[i]]
        for j in range(len(convexID)):
            convex2 = data_2dPoints[convexID[j]]
            if longest < destance(convex1, convex2):
                p1 = convexID[i]
                p2 = convexID[j]
                longest = destance(convex1, convex2)
    # print("直径:", longest, "最远两点id:", p1, p2)

    # 计算椭圆的b边:(刚才两点最长作为a边,现在还需要算椭圆的短边)
    ## idea: 根据最长边,把convex hull 的点分为两坨,然后找到这两坨之间,最小的距离,就是b了
    ## step1: 计算划分线:
    x1 = data_2dPoints[p1][0]
    y1 = data_2dPoints[p1][1]
    x2 = data_2dPoints[p2][0]
    y2 = data_2dPoints[p2][1]
    k = (y1 - y2) / (x1 - x2)
    b = y1 - k * x1

    # 分类:
    group1 = []
    group2 = []
    for i in range(len(convexID)):
        if convexID[i] == p1 or convexID[i]==p2:
            continue
        Xnow=data_2dPoints[convexID[i]][0]
        Ynow=data_2dPoints[convexID[i]][1]
        y_line = k* Xnow+b
        if Ynow>y_line:
            group1.append(convexID[i])
        if Ynow<y_line:
            group2.append(convexID[i])
    # print("分类结果:",group1,group2)
    # 计算b:
    shortest=99999
    for id1 in group1:
        convex1=data_2dPoints[id1]
        for id2 in group2:
            convex2 = data_2dPoints[id2]
            if shortest > destance(convex1, convex2):
                shortest = destance(convex1, convex2)
    # print(shortest,longest)

    # 计算密度：
    amount = len(data_2dPoints)
    # print("总数量", amount)
    # area = math.pi * pow(longest, 2)
    area = math.pi * longest * shortest
    density = amount / area
    return density


# 全部数据：
# data = pd.read_csv("Data/parks.csv").to_numpy(str).T[0:2].T
# data_convert = data.astype(float).tolist()
# print(calculateDensity(data_convert))

# cluster分类：
clusterList = test_k_means()
for data in clusterList:
    print("density：", calculateDensity(data))

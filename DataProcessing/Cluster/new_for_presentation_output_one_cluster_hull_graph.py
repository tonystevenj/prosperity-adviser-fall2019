#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: k_means.py

@desc: k_means 聚类算法

@hint:
"""
import numpy as np
import pandas as pd
import math
import time
import matplotlib.pyplot as plt
def JarvisMarch(S):
    S = np.array(S)
    def angle(u, v):
        x = v[0] - u[0]
        y = v[1] - u[1]
        if y<0:
            class23 = True
        else:
            class23 = False
        if x<0 and y>0:
            class4 = True
        else:
            class4=False
        if y == 0:
            if x == 0:
                return 361
            elif x > 0:
                return 90
            elif x < 0:
                return 270
        out = math.atan(x / y) / math.pi * 180
        if class23:
            out+=180
        if class4:
            out+=360
        return out

    # # test angle method
    # print(angle([0, 0], [0, 1]))
    # print(angle([0, 0], [1, 1]))
    # print(angle([0, 0], [1, 0]))
    # print(angle([0, 0], [1, -1]))
    # print(angle([0, 0], [0, -1]))
    # print(angle([0, 0], [-1, -1]))
    # print(angle([0, 0], [-1, 0]))
    # print(angle([0, 0], [-1, 1]))
    # pass
    # find left most point
    leftmost = 0
    for i in range(len(S)):
        node = S[i]
        if S[leftmost][0]> node[0]:
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
            print("当前对比的两点：",S[nownode],S[i])
            nextDegree = angle(S[nownode],S[i])
            plusDegree = nextDegree-nowDegree

            if plusDegree<0:
                print("负degree,不考虑")
                continue
            if first == True:
                minplusDegree = plusDegree
                first = False
            if plusDegree<=minplusDegree:
                minplusDegree=plusDegree
                minnextDegree = nextDegree
                nextnode = i
            print("nextDegree",nextDegree,"plusDegree",plusDegree,"目前最优的nextnode",nextnode)

        print(nextnode,minnextDegree)
        # time.sleep(1)
        if nextnode == leftmost:
            break
        # 准备下次循环：
        nownode = nextnode
        nowDegree = minnextDegree



    return convexHull

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
    return np.sqrt(np.sum(np.square(vec1 - vec2)))  #注意这里的减号

def loadDataSet():
    # dataSet = np.loadtxt("Data/dataSet.csv")
    # print(len(dataSet))
    # print(type(dataSet))
    # print(dataSet[0])
    #
    # return dataSet
    import os
    datafilepath = os.path.join("Data/parks.csv")
    data = pd.read_csv(datafilepath).to_numpy(str).T[0:2].T
    data_convert = data.astype(float)
    print(len(data_convert))
    print(data_convert[0])
    print(type(data_convert))
    return data_convert


def initCentroids(dataSet, k):
    # 从数据集中随机选取k个数据返回
    dataSet = list(dataSet)
    print(len(dataSet))
    return random.sample(dataSet, k)

def minDistance(dataSet, centroidList):

    # 对每个属于dataSet的item， 计算item与centroidList中k个质心的距离，找出距离最小的，并将item加入相应的簇类中
    clusterDict = dict() #dict保存簇类结果
    k = len(centroidList)
    for item in dataSet:
        vec1 = item
        flag = -1
        minDis = float("inf") # 初始化为最大值
        for i in range(k):
            vec2 = centroidList[i]
            distance = calcuDistance(vec1, vec2)  # error
            if distance < minDis:
                minDis = distance
                flag = i  # 循环结束时， flag保存与当前item最近的蔟标记
        if flag not in clusterDict.keys():
            clusterDict.setdefault(flag, [])
        clusterDict[flag].append(item)  #加入相应的类别中
    return clusterDict  #不同的类别

def getCentroids(clusterDict):
    #重新计算k个质心
    centroidList = []
    for key in clusterDict.keys():
        centroid = np.mean(clusterDict[key], axis=0)
        centroidList.append(centroid)
    return centroidList  #得到新的质心


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
    colorMark = ['or', 'ob', 'og', 'ok', 'oy', 'ow','oc'] #不同簇类标记，o表示圆形，另一个表示颜色
    centroidMark = ['dr', 'db', 'dg', 'dk', 'dy', 'dw','dc']

    for key in clusterDict.keys():
        plt.plot(centroidList[key][0], centroidList[key][1], centroidMark[key], markersize=12) #质心点
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
    showCluster(centroidList, clusterDict)


    # 找点最多的:

    print("各类长度:")
    max1=0
    for key in clusterDict.keys():
        # print(key)
        print(len(clusterDict[key]))
        if len(clusterDict[max1])<len(clusterDict[key]):
            max1 = key

    return clusterDict[max1]
if __name__ == '__main__':
    # show_fig()
    maxlist=test_k_means()
    print(len(maxlist))
    print(maxlist)
    maxlist1=np.array(maxlist).astype(float)
    output = JarvisMarch(maxlist1)
    print("输出：", output)

    # 画图看看是否正确：
    fig, ax = plt.subplots()
    # 所有点数据：用绿色表示：
    x = maxlist1.T[0].astype(float)
    y = maxlist1.T[1].astype(float)
    n = 750
    scale = 200.0 * np.random.rand(n)
    ax.scatter(x, y, c="green", s=scale, label="green",
               alpha=0.3, edgecolors='none')

    # convex hull算法结果：用红色表示：
    outputnodes = []
    for i in range(len(output)):
        outputnodes.append(maxlist1[output[i]])
    convert1 = np.array(outputnodes)
    x1 = convert1.T[0].astype(float)
    y1 = convert1.T[1].astype(float)
    n = 750
    scale = 200.0 * np.random.rand(n)
    ax.scatter(x1, y1, c="red", s=scale, label="red",
               alpha=0.3, edgecolors='none')

    ax.legend()
    ax.grid(True)
    plt.show()


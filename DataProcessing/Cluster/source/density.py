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

        # print(nextnode,minnextDegree)
        # time.sleep(1)
        if nextnode == leftmost:
            break
        # 准备下次循环：
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
    print("环边输出：", convexID)
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
    print("直径:", longest, "最远两点id:", p1, p2)

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
    print("分类结果:",group1,group2)
    # 计算b:
    b1 = 0
    b2 = 0
    shortest=99999
    for id1 in group1:
        convex1=data_2dPoints[id1]
        for id2 in group2:
            convex2 = data_2dPoints[id2]
            if shortest > destance(convex1, convex2):
                b1=id1
                b2=id2
                shortest = destance(convex1, convex2)
    print("b径:", shortest, "最近两点id:", b1, b2)

    # 计算密度：
    amount = len(data_2dPoints)
    print("总数量", amount)
    # area = math.pi * pow(longest, 2)
    area = math.pi * longest * shortest
    density = amount / area

    # 封装定义的椭圆四个点：
    areaData=[data_2dPoints[p1],data_2dPoints[p2],data_2dPoints[b1],data_2dPoints[b2]]
    return density, convexID, areaData

# 导入数据
import os
dataset_path = '..'
datafilepath = os.path.join(dataset_path, "Data/parks.csv")
data = pd.read_csv(datafilepath).to_numpy(str).T[0:2].T
data_convert=data.astype(float).tolist()

# 计算：
density, convexID, areaData = calculateDensity(data_convert)
print("环边输出：",convexID)
print("密度：",density)
# 画图看看是否正确：
fig, ax = plt.subplots()
# 所有点数据：用绿色表示：
x = data.T[0].astype(float)
y = data.T[1].astype(float)
n = 750
scale = 200.0 * np.random.rand(n)
ax.scatter(x, y, c="green", s=scale, label="green",
           alpha=0.3, edgecolors='none')

# convex hull算法结果：用红色表示：
outputnodes=[]
for i in range(len(convexID)):
    outputnodes.append(data_convert[convexID[i]])
convert1=np.array(outputnodes)
x1= convert1.T[0].astype(float)
y1= convert1.T[1].astype(float)
n = 750
scale = 200.0 * np.random.rand(n)
ax.scatter(x1, y1, c="red", s=scale, label="red",
           alpha=0.3, edgecolors='none')
# area 四个点算法结果：用黑色表示：
convert1=np.array(areaData)
x1= convert1.T[0].astype(float)
y1= convert1.T[1].astype(float)
n = 750
scale = 200.0 * np.random.rand(n)
ax.scatter(x1, y1, c="blue", s=scale, label="blue",
           alpha=0.3, edgecolors='none')

ax.legend()
ax.grid(True)
plt.show()

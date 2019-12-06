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

import os
dataset_path = '..'
datafilepath = os.path.join(dataset_path, "Data/parks.csv")
data = pd.read_csv(datafilepath).to_numpy(str).T[0:2].T
data_convert=data.astype(float).tolist()
# S=[[3,1],[0,0],[2, 0],[1,-1],[2,2],[1, 1],[1,0],]
# print("输出：",JarvisMarch(S))
output = JarvisMarch(data_convert)
print("输出：",output)

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
for i in range(len(output)):
    outputnodes.append(data_convert[output[i]])
convert1=np.array(outputnodes)
x1= convert1.T[0].astype(float)
y1= convert1.T[1].astype(float)
n = 750
scale = 200.0 * np.random.rand(n)
ax.scatter(x1, y1, c="red", s=scale, label="red",
           alpha=0.3, edgecolors='none')

ax.legend()
ax.grid(True)
plt.show()

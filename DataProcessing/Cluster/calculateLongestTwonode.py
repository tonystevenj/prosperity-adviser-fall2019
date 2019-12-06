
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
            nextDegree = angle(S[nownode],S[i])
            plusDegree = nextDegree-nowDegree

            if plusDegree<0:
                continue
            if first == True:
                minplusDegree = plusDegree
                first = False
            if plusDegree<=minplusDegree:
                minplusDegree=plusDegree
                minnextDegree = nextDegree
                nextnode = i
        if nextnode == leftmost:
            break
        nownode = nextnode
        nowDegree = minnextDegree
    return convexHull

def destance(u,v):
    x = v[0] - u[0]
    y = v[1] - u[1]
    return math.sqrt(pow(x,2)+pow(y,2))

data = pd.read_csv("Data/parks.csv").to_numpy(str).T[0:2].T
data_convert=data.astype(float).tolist()
convexID = JarvisMarch(data_convert)
print("输出：",convexID)

# 计算最长两点间最长距离：
longest = 0
for i in range(len(convexID)):
    convex1 = data_convert[convexID[i]]
    for j in range(len(convexID)):
        convex2=data_convert[convexID[j]]
        longest = max(longest,destance(convex1,convex2))
print(longest)

# 计算密度：

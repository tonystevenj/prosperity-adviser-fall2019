from sklearn.cluster import DBSCAN
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot  as plt
# documentation: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html


def showCluster(points2D, labels):
    # 展示聚类结果
    colorMark = ['or', 'ob', 'og', 'ok', 'oy', 'ow','oc'] #不同簇类标记，o表示圆形，另一个表示颜色
    centroidMark = ['dr', 'db', 'dg', 'dk', 'dy', 'dw','dc']
    for i in range(len(points2D)):
        plt.plot(points2D[i][0], points2D[i][1], colorMark[labels[i]])
    plt.show()

dataset_path = '..'
datafilepath = os.path.join(dataset_path, "Data/parks.csv")
# datafilepath = "../Data/parks.csv" # 上面两句话跟他等价
data = pd.read_csv(datafilepath).to_numpy(str).T[0:2].T
data_convert = data.astype(float)
print(len(data_convert))
clustering = DBSCAN(eps=0.03, min_samples=4).fit(data_convert)
print(len(clustering.labels_))
print(clustering.labels_)
print(clustering)
showCluster(data_convert,clustering.labels_)


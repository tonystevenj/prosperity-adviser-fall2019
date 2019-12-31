import ipyvolume as ipv
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from ipywidgets import ColorPicker, VBox, \
    interact, interactive, fixed
import struct
import numpy as np
np.random.seed(12345)

X, _ = make_blobs(n_samples=500, n_features=3, centers=5)

fig = ipv.figure(height=600, width=600, layout={'width':'100%', 'height':'100%'})
scatter = ipv.scatter(*X.T, size=1, marker="sphere")
ipv.xyzlim(-10, 10)
def hex_to_rgb(hex):
    hex = hex[1:]
    return struct.unpack('BBB', bytes.fromhex(hex))
def handle_cp_change(labels, **groups):
    group_ids = [int(g.split(' ')[1]) for g in groups.keys()]
    group_color = {k: hex_to_rgb(get_cp_value(cp)) for k, cp in zip(group_ids, groups.values())}
    colors = list(map(lambda x: group_color[x], labels))
    scatter.color = colors

def get_cp_value(cp):
    if type(cp) == ColorPicker:
        return cp.value
    else:
        return cp
avaliable_colors = {
    0: '#ff0000',
    1: '#00ff00',
    2: '#0000ff',
    3: '#ffff00',
    4: '#00ffff',
    5: '#ff00ff',
    6: '#000000'
}
def color_scatter_with_kmeans(n_clusters):
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans = kmeans.fit(X)
    labels = kmeans.predict(X)
    color_pickers = {f'group {k}': ColorPicker(value=avaliable_colors[k%len(avaliable_colors)], description=f'group {k}')
                     for k in range(n_clusters)}
    handle_cp_change(labels=list(labels), **color_pickers)
    return interact(handle_cp_change, labels=fixed(list(labels)) , **color_pickers)

VBox([fig, interactive(color_scatter_with_kmeans, n_clusters=(1, 10, 1))])
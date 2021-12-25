import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import sklearn.datasets
import umap
import umap.plot
from metric import *
import os


def draw_umap(data, n_neighbors = 15, min_dist = 0.1, n_components = 2, metric = 'euclidean',
              title = 'UMAP'):
    fit = umap.UMAP(
        n_neighbors = n_neighbors,
        min_dist = min_dist,
        n_components = n_components,
        metric = metric
    )
    u = fit.fit_transform(data)
    fig = plt.figure()
    if n_components == 1:
        ax = fig.add_subplot(111)
        ax.scatter(u[:, 0], range(len(u)), c = data)
    if n_components == 2:
        ax = fig.add_subplot(111)
        ax.scatter(u[:, 0], u[:, 1], c = data)
    if n_components == 3:
        ax = fig.add_subplot(111, projection = '3d')
        ax.scatter(u[:, 0], u[:, 1], u[:, 2], c = data, s = 100)
    plt.title(title, fontsize = 18)
    plt.show()


if __name__ == '__main__':

    label = []
    for i in range(1,33):
        data_dir = "data/a" + str(i) + "/mid_data.txt"
        data = pd.read_table(data_dir, header = None)
        data = np.array(data).reshape(1, 15)
        data[0][4] = data[0][4] * 0.6
        BUN = data[0][4]
        Scr = data[0][5]
        ratio = BUN / Scr
        # low:1, normal:2, high:3
        if (ratio < 12):
            label.append(1)
        elif (ratio <= 20):
            label.append(2)
        else:
            label.append(3)
        if (i == 1):
            input = data
        else:
            input = np.vstack((input,data))
    label = np.array(label)

    # np.random.seed(42)
    # input = np.random.rand(800, 15)
    # print(input)
    # draw_umap(data = input, n_neighbors = 20, min_dist = 0.1, n_components = 2, metric = sl_dist)
    # pendigits = sklearn.datasets.load_digits()
    # mnist = sklearn.datasets.fetch_openml('mnist_784')
    # fmnist = sklearn.datasets.fetch_openml('Fashion-MNIST')

    mapper = umap.UMAP(n_neighbors = 15, min_dist = 0.5).fit(input)
    # umap.plot.points(mapper, theme='inferno')
    umap.plot.connectivity(mapper, show_points = True, labels = label)
    # umap.plot.connectivity(mapper, show_points = True, edge_bundling = 'hammer')
    plt.show()

import numpy as np
import pandas as pd

label = []
for i in range(1, 33):
    data_dir = "data/a" + str(i) + "/mid_data.txt"
    data = pd.read_table(data_dir, header = None)
    data = np.array(data).reshape(1, 15)
    data[0][4] = data[0][4] * 0.6
    BUN = data[0][4]
    Scr = data[0][5]
    ratio = BUN / Scr
    # low:1, normal:2, high:3
    label.append(ratio)
    if (i == 1):
        input = data
    else:
        input = np.vstack((input, data))
label = np.array(label)

cluster_1 = [
    input[9],
    input[15],
    input[27]
]

cluster_2 = [
    input[9],
    input[15],
    input[21],
    input[27]
]

cluster_3 = [
    input[7],
    input[8],
    input[13],
    input[14],
    input[19],
    input[20],
    input[25],
    input[26]
]

cluster_4 = [
    input[0]
]

cluster_5 = [
    input[0],
    input[1],
    input[2],
    input[3]
]

cluster_6 = [
    input[28],
    input[29],
    input[30],
    input[31]
]

cluster_7 = [
    input[28]
]

cluster_8 = [
    input[6],
    input[12],
    input[18],
    input[24]
]

cluster_9 = [
    input[5],
    input[6],
    input[11],
    input[12],
    input[18],
    input[24]
]

cluster_10 = [
    input[5],
    input[10],
    input[11],
    input[16],
    input[17],
    input[22],
    input[23]
]

cluster_11 = [
    input[4],
    input[10],
    input[16],
    input[17],
    input[22],
    input[23]
]

cluster_12 = [
    input[4]
]

cluster = [cluster_1, cluster_2, cluster_3, cluster_4,
                    cluster_5, cluster_6, cluster_7, cluster_8,
                    cluster_9, cluster_10, cluster_11, cluster_12]
Aver = []
for cl in cluster:
    shape = np.shape(cl)
    aver = np.sum(cl, axis = 0) / shape[0]
    Aver.append(aver.tolist())

Aver = np.array(Aver).T
f = open('cluster.txt', mode = 'w')
for i, av in enumerate(Aver):
    print(i+1,"\n",av,"\n")
    f.write(str(av.tolist())+"\n\n")


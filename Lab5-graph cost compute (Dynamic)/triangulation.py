import numpy as np
import os
from pprint import pprint


def weight(i, j):
    return ((i[0] - j[0])**2 + (i[1]-j[1])**2)**0.5


# base_path = os.getcwd()+r'\\lab5\\'
# fileName = '66 (Find Second min).txt'
fileName = '66 (Find Second min).txt'
with open(fileName, 'r') as file_:
    lines_ = file_.readlines()
    numNode = int(lines_[0])
    nodes = []
    for i in range(1, len(lines_)):
        nodes.append(tuple([float(j) for j in lines_[i].split(' ')]))
    weight_mx = np.zeros((numNode, numNode))
    for i, nodei in enumerate(nodes):
        for j, nodej in enumerate(nodes):
            if(weight_mx[i][j] > 0) or (i is j):
                continue
            tmp = weight(nodei, nodej)
            weight_mx[i][j] = tmp
            weight_mx[j][i] = tmp


def w(a, b, c):
    global weight_mx
    return weight_mx[a][b] + weight_mx[b][c] + weight_mx[a][c]


def min_weight_triangulation(t, s, n):
    for r in range(1, n - 1):  # every point
        for i in range(1, n - r):
            j = i + r
            t[i][j] = t[i + 1][j] + w(i - 1, i, j)  # create w8 4 base
            s[i][j] = i
            for k in range(i + 1, j):
                u = t[i][k] + t[k + 1][j] + w(i - 1, k, j)
                if u < t[i][j]:
                    t[i][j] = u
                    s[i][j] = k
        print()
        pprint(t)
    return t[1][n-1]


def traceback(i, j, s):
    global tracks
    if i == j:
        return
    traceback(i, s[i][j], s)
    traceback(s[i][j] + 1, j, s)
    tracks.append((i - 1, j, s[i][j]))


# print(dict(enumerate(nodes)))
n = numNode
t = []
s = []
score = []
# Create array of nxn, fill with zero
for i in range(0, n):
    t.append([])
    s.append([])
    for j in range(0, n):
        t[i].append(0)
        s[i].append(0)
# DP
print("Optimal split weight:" + str(min_weight_triangulation(t, s, n)))
# pprint(s)
tracks = []
traceback(1, n-1, s)
# print(tracks)

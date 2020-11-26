from itertools import combinations
import numpy as np
import os


def weight(i, j):
    return ((i[0] - j[0])**2 + (i[1]-j[1])**2)**0.5


# base_path = os.getcwd()+r'\\lab5\\'
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


l = list(range(0, numNode))
lc = []
for i in l:
    lc.append((l[i], l[i-1], l[i-2]))
soln = []
score = []
for base in lc:
    n_ = []
    for node in l:
        if node not in base:
            n_.append(node)
    w1Node = (n_[0], base[1], base[0])
    w2Node = (n_[1], base[1], base[2])
    w3Node = (n_[0], base[1], n_[1])
    # print(w1Node)
    # print(w2Node)
    # print(w3Node)
    w1 = w(n_[0], base[1], base[0])
    w2 = w(n_[1], base[1], base[2])
    w3 = w(n_[0], n_[1], base[1])
    score.append(w1+w2+w3)
    print(w1+w2+w3)
    print(w1Node, w2Node, w3Node)
    print()
    soln.append([w1+w2+w3, (w1Node, w2Node, w3Node)])
print(sorted(set(score)))

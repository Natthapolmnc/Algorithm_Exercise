import numpy as np
import copy

fileName = '7_extra2'
with open(fileName+'.txt') as file_:
    totalVertex, _, _ = [int(i) for i in file_.readline().strip().split(' ')]
    graph = np.zeros((totalVertex, totalVertex), dtype='int').tolist()
    askPath = []
    for line in file_.readlines():
        tmp = [i for i in line.split()]
        if(len(tmp) == 3):
            from_, to_, weight_ = tmp
            weight_ = int(weight_)
            graph[int(from_)-1][int(to_)-1] = weight_
            # graph[int(to_)-1][int(from_)-1] = weight_
        elif(len(tmp) == 2):
            askPath.append([int(i) for i in tmp])


def adj(node):
    return [idx for idx, val in enumerate(graph[node]) if val != 0]


def printPath(parent, i, j):
    if(i is j):
        print(i)
    elif(parent[i][j] is None):
        print('No path')
    else:
        printPath(parent, i, parent[i][j])
        print(j)


def FloydWarshall(graph):
    global parent
    NUM_NODES = len(graph)
    INF = float('inf')
    distance = copy.deepcopy(graph)
    parent = copy.deepcopy(graph)
    for i in range(NUM_NODES):
        for j in range(NUM_NODES):
            # for distance matrix
            if (i is j):
                distance[i][j] = 0
            elif(distance[i][j] is 0):
                distance[i][j] = INF
            # for parent matrix
            if((i is j) or (distance[i][j] is INF)):
                parent[i][j] = None
            else:
                parent[i][j] = i
    for k in range(NUM_NODES):
        for i in range(NUM_NODES):
            for j in range(NUM_NODES):
                # for parent matrix
                if(distance[i][j] > max(distance[i][k], distance[k][j])):
                    parent[i][j] = parent[k][j]
                # for distance matrix
                distance[i][j] = min(distance[i][j], max(distance[i][k], distance[k][j]))
    print(distance)
    print()
    print(parent)


# print(graph)
parent = None
FloydWarshall(graph)
printPath(parent, 4, 3)
# for p in askPath:
# allPath = []
# printPath(parent, 0, 6)
# print(p)
# printAllPaths(p[0]-1, p[1]-1)

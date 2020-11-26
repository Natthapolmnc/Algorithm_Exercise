import math
import copy

def distance(i, j):
    return math.sqrt(math.pow(i[0]-j[0],2) + math.pow(i[1]-j[1],2))

def cost(points, i, j, k):
    p1 = points[i]
    p2 = points[j]
    p3 = points[k]
    return distance(p1, p2) + distance(p2, p3) + distance(p3, p1)

def isPointAdjacent(i,j,points):
    temp=False
    distance(points[i],points[j])
    for k in points:
        if (k!=points[i]):
            if temp:
                if distance(points[i],k)<distance(points[i],points[j]):
                    return False
            if distance(points[i],k)<distance(points[i],points[j]):
                temp = True
    return True
    

def minimumCost(points, n):
    zimbaTable = [[0 for x in range(n)]for x in range(n)]
    minTriangleTrack = copy.deepcopy(zimbaTable)
    minPointTrack = copy.deepcopy(zimbaTable)
    MAX = 100000.0
    if n<3:
        return 0
    cnt = 0
    while(cnt<n):
        i = 0
        j = cnt
        while j<n:
            if(j<i+2):
                zimbaTable[i][j] = 0.0
            else:
                zimbaTable[i][j] = MAX
                k = i+1
         
                while(k<j):
                    val = zimbaTable[i][k] + zimbaTable[k][j] + cost(points, i, j ,k)
                    if(zimbaTable[i][j]>val):
                        ans=[]
                        if zimbaTable[i][k]!=0:
                            for x in minPointTrack[i][k]:
                                # print(x)
                                ans.append(x)
                        if zimbaTable[k][j]!=0:
                            for x in minPointTrack[k][j]:
                                # print(x)
                                ans.append(x)

                        minTriangleTrack[i][j] = (i,k,j)

                        if not isPointAdjacent(i,j,points):
                            if (i,j) not in ans:
                                ans.append((i,j))
                        elif not isPointAdjacent(k,j,points):
                            if (k,j) not in ans:
                                ans.append((k,j))
                        elif not isPointAdjacent(i,k,points):
                            if (i,k) not in ans:
                                ans.append((i,k))

                        minPointTrack[i][j]=ans

                        zimbaTable[i][j] = val
                    k+=1
            i+=1
            j+=1
        cnt+=1
    return zimbaTable[0][n-1],minPointTrack[0][n-1]

def read(file):
    with open(file, "r") as p:
        num_point=int(p.readline().strip())
        lst_p=[]
        for i in p:
            lst_p.append(tuple(map(float,i.split())))
        return (num_point,lst_p)

prob=read("7 Extra.txt")

answer = minimumCost(prob[1], prob[0])
print("The minimum cost is", answer[0])
from itertools import combinations

def ver_cov_k(graph_file):
    k,graph,edges=read_graph(graph_file)
    comb=list(combinations(list(graph.keys()),k))
    ans={}
    for k in comb:
        for i in edges:
            fnd=False
            for j in range(len(i)):
                if (i[j] in k):
                    fnd=True
                    continue
            if (fnd==False):
                break
        ans[k]=fnd
    hav_ans=False
    for i in list(ans.keys()):
        if (ans[i]):
            hav_ans=True
            print("Yes")
            break
    if (hav_ans==False):
        print ("No")
    for i in list(ans.keys()):
        if (ans[i]):
            print (i)            

def read_graph(file):
    graph={}
    edges=[]
    k=0
    with open(file,"r") as p:
        index=1
        k=int(p.readline())
        for i in p:
            line=list(map(int,i.split()))
            graph[index]=[]
            for j in range(len(line)):
                if (line[j]==1):
                    edges.append((index,j+1))
                    graph[index].append(j+1)
            index+=1
    return (k,graph,edges)

ver_cov_k("1.5.txt")
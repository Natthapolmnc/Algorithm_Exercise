from itertools import combinations

def ver_cov_app(graph_file):
    graph=read_graph(graph_file)
    visited={}
    for i in list(graph.keys()):
        visited[i]=False
    for i in list(graph.keys()):
        if not (visited[i]):
            for j in graph[i]:
                if not visited[j]:
                    visited[j]=True
                    visited[i]=True
                    break
    k=0
    str_res=""
    for i in list(visited.keys()):
        if visited[i]:
            k+=1
            str_res+=str(i)+" "
    print (str_res)
    print (k)

def read_graph(file):
    graph={}
    with open(file,"r") as p:
        index=1
        for i in p:
            line=list(map(int,i.split()))
            graph[index]=[]
            for j in range(len(line)):
                if (line[j]==1):
                    graph[index].append(j+1)
            index+=1
    return (graph)

ver_cov_app("q2.txt")
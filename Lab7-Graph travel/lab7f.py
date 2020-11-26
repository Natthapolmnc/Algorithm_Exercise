def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

def min_weight_in_path(graph,weight,paths):
    min_weight=float("inf")
    min_path=[]
    for i in paths:
        max_weight_in_path=float("inf")*-1
        for j in range(len(i)-1):
            weight_o_pair=weight[(i[j],i[j+1])]
            if (weight_o_pair>max_weight_in_path):
                max_weight_in_path=weight_o_pair
                max_path=i
        if (max_weight_in_path<min_weight):
            min_weight=max_weight_in_path
            min_path=max_path
    return (min_weight,min_path)

def do(filename):
    with open(filename,"r") as p:
        num_place,num_road,num_quest=tuple(map(int,p.readline().split()))
        if ((num_place,num_road)==(0,0)):
            return
        graph={}
        weight_graph={}
        for i in range(1,num_place+1):
            graph[i]=[]
        for i in range(1,num_place+1):
            for j in range(1,num_place+1):
                weight_graph[(i,j)]=0
        for i in range(num_road):
            from_,to_,weight=tuple(map(int,p.readline().split()))
            graph[from_].append(to_)
            graph[to_].append(from_)
            weight_graph[(from_,to_)]=weight
            weight_graph[(to_,from_)]=weight
        for i in range(num_quest):
            from_,to_=tuple(map(int,p.readline().split()))
            print(from_," to ",to_)
            paths=find_all_paths(graph,from_,to_)
            if (paths==[]):
                print("No path.")
                continue
            min_weight,min_path=min_weight_in_path(graph,weight_graph,paths)
            print(min_weight)
            print("path: ",min_path)
            
do("7.02")

            

visitedOrder=[]
def reverseOrder(graph):
    global visitedOrder
    for i in graph.keys():
        if (i not in visitedOrder):
            fillOrder(i,graph)
    visitedOrder=[]
 
orderStack=[]
def fillOrder(v, graph):
    global orderStack 
    global visitedOrder
    visitedOrder.append(v)
    for i in graph[v]: 
        if i not in visitedOrder: 
            fillOrder(i,graph) 
    orderStack.append(v)
    


def graphTranspose(graph):
    trans_graph={}
    for i in graph.keys():
        trans_graph[i]=[]
    for i in graph.keys():
        for j in graph[i]:
            trans_graph[j].append(i)
    return trans_graph
    
def SCCs(graph):
    global orderStack
    reverseOrder(graph)
    stack=orderStack
    Tgraph=graphTranspose(graph)
    visited=[]
    SCCs_graph={}
    SCCs_node=[]
    while stack:
        node=stack.pop()
        if (node not in visited):
            temp_stack=[]
            temp_stack.append(node)
            new_SCC_node=[]
            while temp_stack:
                subnode=temp_stack.pop()
                if (subnode not in visited):
                    visited.insert(0,subnode)
                    new_SCC_node.append(subnode)
                    temp_stack.extend(Tgraph[subnode])
                else:
                    continue
            SCCs_node.append(new_SCC_node)
    for nodes in SCCs_node:
        SCCs_graph[tuple(nodes)]=[]
    for nodes in SCCs_node:
        for node in nodes:
            for dest in graph[node]:
                for chk_nodes in SCCs_node:
                    if (dest in chk_nodes and dest not in nodes):
                        SCCs_graph[tuple(nodes)].append(tuple(chk_nodes))
    orderStack=[]
    return SCCs_graph


def test(filename):
    global orderStack
    with open(filename,"r") as p:
        while (True):
            num_place,num_road=tuple(map(int,p.readline().split()))
            if ((num_place,num_road)==(0,0)):
                return
            graph={}
            for i in range(1,num_place+1):
                graph[i]=[]
            for i in range(num_road):
                from_,to_,road=tuple(map(int,p.readline().split()))
                if (road==1):
                    graph[from_].append(to_)
                elif (road==2):
                    graph[from_].append(to_)
                    graph[to_].append(from_)
            ans=lambda x : 1 if x==1 else 0 
            print (SCCs(graph).keys())
            


def do(filename):
    with open(filename,"r") as p:
        while (True):
            num_place,num_road=tuple(map(int,p.readline().split()))
            if ((num_place,num_road)==(0,0)):
                return
            graph={}
            for i in range(1,num_place+1):
                graph[i]=[]
            for i in range(num_road):
                from_,to_,road=tuple(map(int,p.readline().split()))
                if (road==1):
                    graph[from_].append(to_)
                elif (road==2):
                    graph[from_].append(to_)
                    graph[to_].append(from_)
            ans=lambda x : 1 if x==1 else 0 
            print (ans(len(list(SCCs(graph).keys()))))
           
def do_task_count(filename):
    with open(filename,"r") as p:
        while (True):
            num_place,num_road=tuple(map(int,p.readline().split()))
            if ((num_place,num_road)==(0,0)):
                return
            graph={}
            for i in range(1,num_place+1):
                graph[i]=[]
            for i in range(num_road):
                from_,to_,road=tuple(map(int,p.readline().split()))
                if (road==1):
                    graph[from_].append(to_)
                elif (road==2):
                    graph[from_].append(to_)
                    graph[to_].append(from_)
            print (len(list(SCCs(graph).keys())))

def do_weak(filename):
    with open(filename,"r") as p:
        while (True):
            num_place,num_road=tuple(map(int,p.readline().split()))
            if ((num_place,num_road)==(0,0)):
                return
            graph={}
            for i in range(1,num_place+1):
                graph[i]=[]
            for i in range(num_road):
                from_,to_,road=tuple(map(int,p.readline().split()))
                if (road==1):
                    graph[from_].append(to_)
                    graph[to_].append(from_)
                elif (road==2):
                    graph[from_].append(to_)
                    graph[to_].append(from_)
            ans=lambda x : 1 if x==1 else 0 
            print (ans(len(list(SCCs(graph).keys()))))

def do_fill(filename):
    with open(filename,"r") as p:
        while (True):
            num_place,num_road=tuple(map(int,p.readline().split()))
            if ((num_place,num_road)==(0,0)):
                return
            graph={}
            for i in range(1,num_place+1):
                graph[i]=[]
            for i in range(num_road):
                from_,to_,road=tuple(map(int,p.readline().split()))
                if (road==1):
                    graph[from_].append(to_)
                elif (road==2):
                    graph[from_].append(to_)
                    graph[to_].append(from_)
            scc_graph=SCCs(graph)
            finish=False
            while(not finish):
                finish=True
                min_=1000
                min_lst=[]
                for i in scc_graph.keys():
                    stack=[i]
                    visited=[]
                    while (stack):
                        node=stack.pop()
                        if (node not in visited):
                            visited.append(node)
                            stack.extend(scc_graph[node])
                    if (len(visited)<min_):
                        min_=len(visited)
                        min_lst=visited
                        start_node=i
                max_=0
                include_node=0
                do_you_do=False
                for i in scc_graph.keys():
                    cnt=0
                    stack=[i]
                    visited=[]
                    while (stack):
                        node=stack.pop()
                        if (node not in visited):
                            visited.append(node)
                            stack.extend(scc_graph[node])
                    temp_lst=[i for i in list(scc_graph.keys()) if (i not in min_lst)]
                    for j in temp_lst:
                        if (j in visited):
                            cnt+=1
                    if (cnt>max_):
                        do_you_do=True
                        finish=False
                        max_=cnt
                        include_node=i
                if (not do_you_do):
                    temp_lst=[i for i in list(scc_graph.keys()) if (i not in min_lst)]
                    for i in temp_lst:
                        print (min_lst[-1],end="")
                        print ("==>",end="")
                        print (i)
                        scc_graph[min_lst[-1]].append(i)
                        finish=False
                if (include_node!=0 and do_you_do):
                    print (min_lst[-1],end="")
                    print ("==>",end="")
                    print (include_node)
                    scc_graph[min_lst[-1]].append(include_node)
            print ("=======================================================================")



do_weak("Extra6.7.txt")
#1223
graph_g={"a":["b","d"],"b":["a","d"],"d":["a","b"]}


def loop (graph):
    res=[]
    for i in graph.keys():
        for j in graph.keys():
            for k in find_all_paths(graph, i, j, path=[]):
                res.append(k)
    return res


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
        
def filter_hamil_path(graph):
    hamil=[]
    for i in loop(graph):
        if (len(i)==len(graph.keys())):
            hamil.append(i)
    return hamil

def filter_hamil_cycle(graph):
    hamil=[]
    for i in loop(graph):
        if (len(i)==len(graph.keys()) and (i[0] in graph[i[-1]])):
            hamil.append(i)
    return hamil

def fill_hamil(graph):
    hamil=[]
    for i in loop(graph):
        if (len(i)==len(graph.keys()) and (i[0] in graph[i[-1]])):
            return "have hamil cycle"
        elif (len(i)==len(graph.keys())):
            return print (i[-1],"->",i[0])

def inputt (f):
    theDict = {y-64:chr(y) for y in range(65,91)}
    Gdict={}
    i=1
    readf=f.readline()
    while readf != '':
      mlist=readf.strip('\n').split(" ")
      Gdict[theDict[i]] = []
      for j in range(len(mlist)):
          if int(mlist[j]) > 0:
              Gdict[theDict[i]].append(theDict[j+1])
      readf=f.readline()
      i=i+1
    # print(Gdict)
    return Gdict

file=open("2.2.4.txt","r")
print (len(filter_hamil_cycle(inputt(file))))
file.close()


def reduc_sat2ver(filename):
    graph,k,K, claus_num=prob_read(filename)
    print (k)
    print (K)
    clas_lst=[i for i in list(graph.keys()) if len(i.split("_"))>1]
    val_lst=[i for i in list(graph.keys()) if len(i.split("_"))==1]
    indx_dict={}
    cnt_indx=0
    for i in val_lst:
        indx_dict[i]=cnt_indx
        cnt_indx+=1
    for j in clas_lst:
        indx_dict[j]=cnt_indx
        cnt_indx+=1
    res=[]
    for i in range(k):
        res.append([0]*k)
    for i in val_lst:
        for j in graph[i]:
            res[0][6]=1
            res[indx_dict[i]][indx_dict[j]]=1
    for i in clas_lst:
        for j in graph[i]:
            res[indx_dict[i]][indx_dict[j]]=1
    pret_print(res)

                
def pret_print(mat):
    for i in mat:
        for j in i:
            print(j,end=" ")
        print ()

def prob_read(file):
    graph={}
    with open(file,"r") as p:
        claus_num=int(p.readline())
        var_num=0
        indx_claus=0
        for i in p:
            claus=list(map(int,i.split()))
            for var in claus:
                if var_num<abs(var):
                    var_num=abs(var)
                if not(str(var) in list(graph.keys())):
                    graph[str(var)]=[]
                    graph[str(var)].append(str(var*-1))
                    graph[str(var*-1)]=[]
                    graph[str(var*-1)].append(str(var))
                graph[str(indx_claus)+"_"+str(var)]=[]
            graph[str(indx_claus)+"_"+str(claus[0])].extend([str(indx_claus)+"_"+str(claus[1]),str(str(indx_claus)+"_"+str(claus[2])),str(claus[0])])
            graph[str(claus[0])].append(str(indx_claus)+"_"+str(claus[0]))
            graph[str(indx_claus)+"_"+str(claus[1])].extend([str(indx_claus)+"_"+str(claus[0]),str(str(indx_claus)+"_"+str(claus[2])),str(claus[1])])
            graph[str(claus[1])].append(str(indx_claus)+"_"+str(claus[1]))
            graph[str(str(indx_claus)+"_"+str(claus[2]))].extend([str(indx_claus)+"_"+str(claus[0]),str(indx_claus)+"_"+str(claus[1]),str(claus[2])])
            graph[str(claus[2])].append(str(str(indx_claus)+"_"+str(claus[2])))
            indx_claus+=1
        k=var_num*2+indx_claus*3
        K=var_num+indx_claus*3
        print (list(graph.keys()))
        return (graph,k,K,claus_num)

    
# prob_read("q3.txt")
reduc_sat2ver("q3.txt")
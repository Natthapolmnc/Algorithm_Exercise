the=["G","P","P","G","P"]
k=1

def brute_grab (arr,k):
    i=0
    all=[]
    print (arr)
    while i < len(arr):
        if arr[i]=='G':
            G = arr[i]+str(i)
            for j in range(k+1):
                if (i-j)>-1 and arr[i-j]=='P':
                  #print(G,arr[i-j]+str(i-j))
                  all.append([G,arr[i-j]+str(i-j)])
            for z in range(k+1):     
                if (i+z)<len(arr) and arr[i+z]=='P' :
                  #print(G,arr[i+z]+str(i+z))
                  all.append([G,arr[i+z]+str(i+z)])
        i=i+1
    # print(all,"\n","-----------------")
    all_combi=combinations([],all)
    result=[]
    max_len=len(all_combi[0])
    for i in all_combi:
        max_len=max([max_len,len(i)])
    for i in all_combi:
        if (len(i)==max_len):
            result.append(i)
    print ("max passenger : "+str(max_len))
    print ("way to pick: "+str(len(result)))
        
    


def combinations(target,data,res=[]):
    for i in range(len(data)):
        new_target = target.copy()
        new_data = data.copy()
        new_target.append(data[i])
        new_data = data[i+1:]
        ni = True
        mi = []
        for i in new_target:
            if i[0] not in mi and i[1] not in mi:
                mi.append(i[0])
                mi.append(i[1])
            else:
                ni = False
        if ni == True:
            res.append(new_target)
            mac=len(new_target)
        combinations(new_target,new_data,res)
    return res


def greed_grab(lst,k):
    temp_lst=lst.copy()
    path=[]
    for i in range(len(temp_lst)):
        if (temp_lst[i]=="G"):
            found=False
            for j in range(k,0,-1):
                if (i-j<0):
                    continue
                elif (i-j>0):
                    if (temp_lst[i-j]=="P"):
                        path.append("G: "+str(i)+", P:"+str(int(i-j)))
                        temp_lst[i-j]="emp"
                        found=True
                        break
            if (found):
                continue
            for l in range(1,k+1):
                if (l+i>len(lst)-1):
                    continue
                else:
                    if (temp_lst[l+i]=="P"):
                        path.append("G: "+str(i)+", P:"+str(int(l+i)))
                        temp_lst[l+i]="emp"
                        found=True
                        break
    print ("path\t: "+str(path))
    print ("maximum passenger: "+str(path))
    return path

def read_prob(filename):
    with open(filename,"r") as file:
        result=[]
        k=0
        fst_line=True
        for i in file:
            if (fst_line):
                for j in i.strip():
                    result.append(j)
            else:
                k=int(i)
            fst_line=False
        return (result,k)
        



arr,k=read_prob("3.1.3.txt")
brute_grab(arr,k)
greed_grab(arr,k)
                    
                    


            
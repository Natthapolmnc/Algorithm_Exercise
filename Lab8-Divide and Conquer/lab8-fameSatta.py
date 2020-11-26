def qd(n):
    lst=[i for i in range(1,n+1)]
    nwNormalMerge(lst)
    print (result)

result=[]
def nwNormalMerge(lst):
    even=[lst[i] for i in range(len(lst)) if i%2==0]
    odd=[lst[i] for i in range(len(lst)) if i%2==1]
    if (len(lst)==1):
        result.append(lst[0])
        return
    nwNormalMerge(even)
    nwNormalMerge(odd)

qd(8)
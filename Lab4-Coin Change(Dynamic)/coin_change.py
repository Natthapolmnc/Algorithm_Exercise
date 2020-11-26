import sys

sys.setrecursionlimit(10000000)

def mincoin(S,n):
    return count(S,len(S),n)

def count(S, m, n): 
    S.sort()
    table = [[0 for x in range(m)] for x in range(n+1)] 
    for i in range(1, n+1):
        minimum = float('inf')
        for j in range(m): 
            if(i >= S[j]):
                minimum = min(minimum, 1+table[i-S[j]][j])
            table[i][j] = minimum
    back_tracking(S,table,n)
    return table

def back_tracking(s,point,n):
    P =[]
    i=len(s)-1
    j=n
    while (i>=0 and j>0):
        if(j>=s[i] and point[j][i] == (1+point[j-s[i]][i]) ):
            P.append(s[i])
            j=j-s[i]
        else:
            i=i-1
    print("Amount =",n)
    # print("coins [] =",s)
    print("Minimum of Coin is ",len(P))
    print(P)
    return P

def findAllChanges(S,n,index_s=0,dyna_dict={}):
    if n==0:
        dyna_dict[(index_s,n)]=[[]]
    else:
        res=[]
        for i in range(index_s,len(S)):
            if (S[i]<=n):
                pre_res=findAllChanges(S,n-S[i],i,dyna_dict)
                res.extend([[S[i]]+l for l in pre_res])
        dyna_dict[(index_s,n)]=res
    return dyna_dict[(index_s,n)]

def read_case(filename):
    with open(filename,"r") as file:
        n=int(file.readline())
        S=list(map(int,file.readline().split()))
        lst=findAllChanges(S,n)
        if (lst):
            print ("All path :", end=" ")
            print (findAllChanges(S,n))
            mincoin(S,n)
        else:
            print ("No min case")

read_case("4.1.txt")


            
    

    

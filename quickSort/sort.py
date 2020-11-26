lst=[1,4,5,2]

def quickSort(lst,start,stop):
    if(start<stop):
        q=partition(lst,start,stop)
        quickSort(lst,start,q-1)
        quickSort(lst,q+1,stop)
        
def partition(lst,start,stop):
    x=lst[stop]
    i=start-1
    for j in range(start,stop-1):
        if lst[j]<=x:
            i+=1
            lst[j],lst[i]=lst[i],lst[j]
    lst[i+1],lst[stop]=lst[stop],lst[i+1]
    return i+1

quickSort(lst,0,len(lst)-1)
print (lst)

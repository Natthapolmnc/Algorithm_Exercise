import math

def sort(n):
    lst=[i for i in range(n+1)]
    even=[i for i in lst if i%2==0]
    odd=[i for i in lst if i%2==1]
    divide(0,len(even)-1,even)
    divide(0,len(odd)-1,odd)
    even.extend(odd)
    print (even)
    
def conquer(start,stop,lst):
    for i in range(start+1,stop):
        if (lst[i]==(lst[start]+lst[stop])/2):
            lst[i], lst[stop]=lst[stop],lst[i]
        if (lst[i]==(lst[start+1]+lst[stop])/2):
            lst[i], lst[stop]=lst[stop],lst[i]
        if (lst[i]==(lst[start]+lst[stop-1])/2):
            lst[i], lst[stop-1]=lst[stop-1], lst[i]

def divide(start,stop,lst):
    if (((stop-start)+1)<3):
        return
    if (((stop-start)+1)==3 or ((stop-start)+1)==4):
        conquer(start,stop,lst)
    else:
        middle=math.floor((stop-start)/2)
        divide(start,middle,lst)
        divide(middle+1,stop,lst)

def combine(start1,stop1,start2,stop2,lst): #have to fix
    pointer_l=start1
    pointer_r=stop2
    while (True):
        checker=(lst[pointer_l]+lst[pointer_r])/2
        checker=(lst[stop1]+lst[stop2])
        for i in range(start1+1,stop2):
            if (i==checker):
                lst[pointer_r],lst[i]=lst[i],lst[pointer_r]

    
sort(4)
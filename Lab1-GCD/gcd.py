import sys
import matplotlib.pyplot as plt


sys.setrecursionlimit(150000)

def FindGCD1(m,n):
    if (m==0 or n==0):
        return (0,1)
    m=abs(m)
    n=abs(n)
    t=min(m,n)
    cal_times=0
    while m%t!=0 or n%t!=0:
        t=t-1
        cal_times+=1
    return (t,cal_times)

def FindGCD2(m, n):
    if (m==0 or n==0):
        return (0,1)
    m=abs(m)
    n=abs(n)
    m_primes, m_cal_num=prime_factor(m)
    n_primes, n_cal_num=prime_factor(n)
    cal_num=m_cal_num+n_cal_num
    com_mul=1
    for i in m_primes:
        for j in n_primes:
            if (i==j):
                com_mul=com_mul*i
                n_primes.remove(j)
                cal_num+=1
                break
    return (com_mul,cal_num)

def prime_factor(main_num,cal_times=0):
    t=main_num
    primes=[]
    i=1
    while (t!=1):
        if (t%i==0):
            t=t/i
            primes.append(i)
            i=1
        i+=1
        cal_times+=1
    return (primes, cal_times)

def FindGCD3(m,n,cal_times=0):
    if (m==0 or n==0):
        return (0,1)
    m=abs(m)
    n=abs(n)
    if m==n:
        return (m,cal_times)
    elif m>n:
        if (m%n==0):
            return (n,cal_times)
        return FindGCD3(m%n,n,cal_times+1)
    elif m<n:
        if (n%m==0):
            return (m,cal_times)
        return FindGCD3(n%m,m,cal_times+1)

def MultiGCD(set_m):
    result=0
    m=set_m[0]
    n=set_m[1]
    m=abs(m)
    n=abs(n)
    result,cal_times=FindGCD3(m,n)
    for i in range(2,len(set_m)):
        result,nw_cal=FindGCD3(result,set_m[i])
        cal_times+=nw_cal
    return (result,cal_times)


# case=open("GCD\Case1.txt","r")
# for i in case:
#     m,n=map(int,i.split())
#     gcd1,cal1=FindGCD1(m,n)
#     print ("GCD 1: "+str(gcd1)+"\nGCD1 times of calculation: "+str(cal1))
#     gcd2,cal2=FindGCD2(m,n)
#     print ("GCD 2: "+str(gcd2)+"\nGCD2 times of calculation: "+str(cal2))
#     gcd3,cal3=FindGCD3(m,n)
#     print ("GCD 3: "+str(gcd3)+"\nGCD3 times of calculation: "+str(cal3))

# case.close()

# extra_case_1=open("GCD\Extra Case1.txt","r")
# for i in extra_case_1:
#     m_list=map(int,i.split())
#     gdc_extra,cal_extra=MultiGCD(list(m_list))
#     print ("Extra1: GCD extra "+str(gdc_extra)+"\nextra1 caltime:"+str(cal_extra))
# extra_case_1.close()

# extra_case_2=open("GCD\Extra Case2.txt","r")
# for i in extra_case_2:
#     m_list=map(int,i.split())
#     gdc_extra,cal_extra=MultiGCD(list(m_list))
#     print ("Extra2: GCD extra "+str(gdc_extra)+"\nextra2 caltime:"+str(cal_extra))
# extra_case_2.close()

# print("\n\n\n EXTRA CASE 3\n\n\n")


extra_case_3=open("Extra Case3.txt","r")
for i in extra_case_3:
    m,n=map(int,i.split(","))
    gcd1,cal1=FindGCD3(m,n)
    print ("GCD 1: "+str(gcd1)+"\nGCD1 times of calculation: "+str(cal1))

extra_case_3.close()
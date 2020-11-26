import math
import sys
sys.setrecursionlimit(5000)

def distant_cal(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

def sort_graph(lst_p):
    sort_lst=lst_p.copy()
    for i in range(0,len(lst_p)):
        this_p=lst_p[i]
        min_dis=float('inf')
        min_index=i
        for j in range(i+1,len(lst_p)):
            if min_dis>distant_cal(this_p,lst_p[j]):
                min_dis=distant_cal(this_p,lst_p[j])
                min_index=j
        if (i+1<len(lst_p)):
            sort_lst[i+1],sort_lst[min_index]=sort_lst[min_index] ,sort_lst[i+1]
    return sort_lst

trianglee={}
dyna_dict={}

# def cost_weight(num_point,lst_p):
#     global dyna_dict
#     lst_p=sort_graph(lst_p)
#     if (tuple(lst_p) in dyna_dict.keys()):
#         return dyna_dict[tuple(lst_p)]
#     if (num_point==3):
#         weight_sum=distant_cal(lst_p[2],lst_p[0])+
#         dyna_dict[tuple(lst_p)]=weight_sum
#         return weight_sum
#     min_weight=float('inf')
#     triangle_list=[]
#     for i in range(len(lst_p)):
#         for j in range(i+2,len(lst_p)-1):
#             first_part=lst_p[i:j+1]
#             second_part=[item for item in lst_p if item not in first_part]
#             second_part.append(lst_p[i])
#             second_part.append(lst_p[j])
#             first_part_weight_cost=cost_weight(len(first_part),first_part)
#             second_part_weght_cost=cost_weight(len(second_part),second_part)
#             new_weight=first_part_weight_cost+second_part_weght_cost
#             if (new_weight<min_weight):
#                 min_weight=new_weight
#                 triangle_list.append(first_part)
#                 triangle_list.append(second_part)
#     dyna_dict[tuple(lst_p)]=min_weight
#     trianglee[tuple(lst_p)]=first_part,second_part
#     for i in range(len(lst_p)-1):
#         min_weight+=distant_cal(lst_p[i],lst_p[i+1])
#     # min_weight+=distant_cal(lst_p[0],lst_p[-1])
#     return min_weight

def cost_weight(num_point,lst_p):
    global dyna_dict
    lst_p=sort_graph(lst_p)
    if (tuple(lst_p) in dyna_dict.keys()):
        return dyna_dict[tuple(lst_p)]
    if (num_point==3):
        weight_sum=distant_cal(lst_p[0],lst_p[1])+distant_cal(lst_p[1],lst_p[2])+distant_cal(lst_p[2],lst_p[0])
        dyna_dict[tuple(lst_p)]=weight_sum
        return weight_sum
    min_weight=float('inf')
    triangle_list=[]
    for i in range(len(lst_p)):
        for j in range(i+2,len(lst_p)-1):
            first_part=lst_p[i:j+1]
            second_part=[item for item in lst_p if item not in first_part]
            second_part.append(lst_p[i])
            second_part.append(lst_p[j])
            first_part_weight_cost=cost_weight(len(first_part),first_part)
            second_part_weght_cost=cost_weight(len(second_part),second_part)
            new_weight=first_part_weight_cost+second_part_weght_cost
            if (new_weight<min_weight):
                min_weight=new_weight
                triangle_list.append(first_part)
                triangle_list.append(second_part)
    dyna_dict[tuple(lst_p)]=min_weight
    trianglee[tuple(lst_p)]=first_part,second_part
    return min_weight

def alltri(key):
    al =[]
    print(" ALL Triangle : ")
    for i in trianglee[tuple(sort_graph(key))]:
        if (len(i)>3):
            i = trianglee[tuple(sort_graph(i))]
        al.append(i)
    print(al)

def read(file):
    with open(file, "r") as p:
        num_point=int(p.readline().strip())
        lst_p=[]
        for i in p:
            lst_p.append(tuple(map(float,i.split())))
        return (num_point,lst_p)
    
prob=read("4.txt")
cost=cost_weight(prob[0],prob[1])
print(" Input :","\n ",prob[1],"\n","Output :","\n ",cost)
alltri(prob[1])




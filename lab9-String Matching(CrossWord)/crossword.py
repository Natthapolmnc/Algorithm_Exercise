def KMPSearch(pat, txt): 
    M = len(pat) 
    N = len(txt) 
    lps = [0]*M 
    j = 0 
    computeLPSArray(pat, M, lps) 
    # print (lps)
    i = 0 # index for txt[] 
    lst=[]
    while i < N: 
        if pat[j] == txt[i]: 
            i += 1
            j += 1
  
        if j == M: 
            lst.append (str(i-j)) 
            j = lps[j-1] 
  
        # mismatch after j matches 
        elif i < N and pat[j] != txt[i]: 
            # Do not match lps[0..lps[j-1]] characters, 
            # they will match anyway 
            if j != 0: 
                j = lps[j-1] 
            else: 
                i += 1
    if (lst!=[]):
        return lst
    return ""
  
def computeLPSArray(pat, M, lps=[]): 
    len_ = 0 # length of the previous longest prefix suffix 
    lps[0] # lps[0] is always 0 
    i = 1
    while i < M: 
        if pat[i]== pat[len_]: 
            len_ += 1
            lps[i] = len_
            i += 1
        else: 
            # This is tricky. Consider the example. 
            # AAACAAAA and i = 7. The idea is similar  
            # to search step. 
            if len_ != 0: 
                len_ = lps[len_-1] 
  
                # Also, note that we do not increment i here 
            else: 
                lps[i] = 0
                i += 1

def crs_wrd(file):
    with open(file,"r") as p:
        lst_of_str=p.readline().split()
        num_row,num_column,len_pat=tuple(map(int,p.readline().split()))
        lst_pat=p.readline().split()
        str_pat=""
        for i in lst_pat:
            str_pat+=i
        crss_mat=[]
        for i in p:
            crss_mat.append(i.split())

        for i in range(num_row):
            str_lr=""
            for j in range(num_column):
                str_lr+=crss_mat[i][j]
            str_rl=str_lr[::-1]
            lr=KMPSearch(str_pat,str_lr)
            if lr!="":
                for l in lr:
                    print (str(i+1)+" "+str(1+int(l))+" "+"LR")
            rl=KMPSearch(str_pat,str_rl)
            if rl!="":
                for l in rl:
                    print (str(i+1)+" "+str(num_column-int(l))+" "+"RL")

        for i in range(num_column):
            str_ub=""
            for j in range(num_row):
                str_ub+=crss_mat[j][i]
            str_bu=str_ub[::-1]
            ub=KMPSearch(str_pat,str_ub)
            if (ub!=""):
                for i in ub:
                    print (str(i+1)+" "+str(1+int(ub))+" "+"UB")
            bu=KMPSearch(str_pat,str_bu)
            if (bu!=""):
                for i in bu:
                    print (str(i+1)+" "+str(num_row-int(bu))+" "+"BU")
        
def crs_wrd_extra(file):
    with open(file,"r") as p:
        lst_of_str=p.readline().split()
        num_row,num_column,len_pat=tuple(map(int,p.readline().split()))
        lst_pat=p.readline().split()
        str_pat=""
        for i in lst_pat:
            str_pat+=i
        crss_mat=[]
        for i in p:
            crss_mat.append(i.split())

        for i in range(num_row):
            str_lr=""
            for j in range(num_column):
                str_lr+=crss_mat[i][j]
            str_lr+=str_lr
            str_rl=str_lr[::-1]
            lr=KMPSearch(str_pat,str_lr)
            if lr!="":
                for z in lr:
                    if (int(z)<num_column):
                        print (str(i+1)+" "+str(1+int(z))+" "+"LR")
            rl=KMPSearch(str_pat,str_rl)
            if rl!="" :
                for z in rl:
                    if (int(z)<num_column):
                        print (str(i+1)+" "+str(num_column-int(z))+" "+"RL")

        for i in range(num_column):
            str_ub=""
            for j in range(num_row):
                str_ub+=crss_mat[j][i]
            str_ub+=str_ub
            str_bu=str_ub[::-1]
            ub=KMPSearch(str_pat,str_ub)
            if (ub!=""):
                for z in ub:
                    if (int(z)<num_row):
                        print (str(1+int(z))+" "+str(i+1)+" "+"UB")
            bu=KMPSearch(str_pat,str_bu)
            if (bu!="" and int(bu!=num_row)):
                for z in bu:
                    if (int(z)<num_row):
                        print (str(num_row-int(z))+" "+str(i+1)+" "+"BU")


crs_wrd_extra("9.3.2.txt")
# computeLPSArray("BAABAA", len("BAABAA"), [0]*len("BAABAA")) 
#f = open("C:\\Users\61337124\2_1_1.txt","r")
f1 = open("2.1.1.txt","r")
#f2 = open("2.1.2.txt","r")
#print(f1.read())
#print(f1.readline())
#print(f2.read())
#f1.close()
#f2.close()

theDict = {y-64:chr(y) for y in range(65,91)}
#print(theDict)
#print(theDict[1])

Gdict={}
i=1
readf=f1.readline()
while readf != '':
    
    mlist=readf.strip('\n').split(" ")
    Gdict[theDict[i]] = []
    for j in range(len(mlist)):
        if mlist[j] == '1':
            test = theDict[j+1]
            print(Gdict[theDict[i]].append("d"))
            # Gdict[theDict[i]] = Gdict[theDict[i]].append(test)

    readf=f1.readline()
    i=i+1
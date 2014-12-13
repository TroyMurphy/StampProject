crit1=[1,8,10,4,3,2,3,4,5]
crit2=[3,5,6,8,9]

def andFilter(self,list1,list2):
    results=[]
    j=0
    for x in list1:
        if x in list2:
            #print x
            results.append(list1[j])
            j+=1
        else:
            j+=1
    mylist=list(set(results))

    return sorted(mylist)

def orFilter(self,list1,list2):
    newlist=sorted(list(set(list1+list2)))
    return newlist

print orFilter(crit1,crit2)
#print andFilter(crit1,crit2)
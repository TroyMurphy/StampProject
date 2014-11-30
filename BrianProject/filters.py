def contains_text(list,string):
    results=[]
    for x in list:
        if string.upper() in x.upper():
            results.append(1)
#            print"True"
        else:
            results.append(0)
#            print"false"
    return results

def and_filter(list1,list2):
    filtered=[]
    for x in list1:
        filtered.append(x*list2[x])
    return filtered

def or_filter(list1,list2):
    filtered=[]
    i=0
    for x in list1:
        if (x or list2[i])==1:
            filtered.append(1)
            i += 1
        else:
            filtered.append(0)
            i += 1
    return filtered

#Test Data

a=[0,1,0,1,0]
b=[1,0,0,0,0]
#=[1,0,1,0,0] AND
#=[1,1,0,1,0] OR


c= and_filter(a,b)
d=or_filter(a,b)

#TESTS FOR FILTERS
#for e in d:
#    print e

#And
#for d in c:
#    print d

#content=["Machine Shop","Saw Work","Noting dkjek","machine shop"]
#test=contains_text(content,"Machine")

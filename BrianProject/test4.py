def orFilter2(list1,list2):
    results=list1
    for i in list2:
        if i not in results:
            results.append(i)
        else:
            pass
    return sorted(results)

list1=[2,3,4,5,7,8,9,10,12]
list2=[1,2,3,15,8]

test=orFilter2(list1,list2)

print test
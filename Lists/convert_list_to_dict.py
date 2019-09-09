
dicfromlist = {i:len(listval) for i in listval}
print(dicfromlist)
newdict = dict.fromkeys(listval, 1)
print(newdict)

newdict1 = {i:listval[i] for i in range(1, len(listval))}
print(newdict1)

l1 = [1,2,3,4,5]
l2 = ["prabhu","viki","nambi","ganesh","karthik"]
zipobj = zip(l1,l2)
dictobj = dict(zipobj)
print(dictobj)

l3 = ["name1", "name2", "name3", "name4", "name5"]
dobj=zip(l3,l2)
dnew = dict(dobj)
print(dnew)


listofTuples = [("Riti" , 11), ("Aadi" , 12), ("Sam" , 13),("John" , 22),("Lucy" , 90)]
studdict = dict(listofTuples)
print(studdict)

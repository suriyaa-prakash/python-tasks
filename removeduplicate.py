mylist=[10,20,30,10,20,40]
newlist=[]
for i in mylist:
    if i not in newlist:
        newlist.append(i)
print(newlist)         
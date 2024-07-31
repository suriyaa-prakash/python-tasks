list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
merge=[]
for i in list1:
    if i not in merge:
        merge.append(i)
for i in list2:
    if i not in merge:
        merge.append(i)        
print(merge)
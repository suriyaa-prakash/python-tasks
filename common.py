a=[1,2,3,4,5,6,7,8]
b=[5,6,7,8,9,10,11]
common=[]
for i in a:
    if i in b:
        common.append(i)
print(common)        
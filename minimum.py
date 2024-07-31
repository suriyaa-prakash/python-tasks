mylist=[1,2,3,7,4,5,6]
min=mylist[0]
for i in range (1,7):
    if min > mylist[i]:
       min = mylist[i]
print(min)    
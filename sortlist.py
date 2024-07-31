list=[3,2,1,5,4]
n=len(list)
for i in range(0,n):
     for j in range(i+1,n):
       if(list[i]>list[j]):
          temp=list[i]
          list[i]=list[j]
          list[j]=temp
print(list)
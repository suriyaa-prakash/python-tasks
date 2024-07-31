class calculator:
 '''def add(self,a,b):
         return a+b
     def add(self,a,b,c=0):
         return a+b+c'''
    
'''def add(self,a = None,b = None,c= None):
            if(a!=None and b!=None and c!=None):
                  print(a+b+c)
            elif(a!=None and b!=None):
                  print(a+b)
            else:
                  print(a)'''
def add (self,*arg):
          total=0
for i in arg:
         total=total+i
return total
   
demo=calculator()
print(demo.add(2,3,5,2,2,3,4))


            

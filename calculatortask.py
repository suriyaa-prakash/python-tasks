class calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def addtion(self):
        return self.num1+self.num2
    def subtration(self):
        return self.num1-self.num2      
num1=int(input("enter"))
num2=int(input("enter"))          
a=calculator(num1,num2)
addition=a.addtion()
print(a.addtion)
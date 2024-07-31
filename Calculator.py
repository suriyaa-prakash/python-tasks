class calculator:
    def __init__(self,num1,num2):
        self.num1=n1
        self.num2=n2
    def addtion(self):
        return self.num1+self.num2
    def subtraction(self):
        return self.num1-self.num2
    def multi(self):
        return self.num1*self.num2
    def division(self):
        return self.num1/self.num2
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))

a=calculator(n1,n2)
addition=a.addtion()
print("The addition result is:",addition)

subtraction=a.subtraction()
print("The subtraction result is:",subtraction)

multi=a.multi()
print("The multification result is:",multi)

division=a.division()
print("The divition result is:",division)


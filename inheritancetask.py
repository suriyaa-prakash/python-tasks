'''class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class employee(person):
    def __init__(self,name,age,emp_id):
        super().__init__(name,age)
        self.emp_id=emp_id
person=person("john",23)
print(person.name,person.age)'''


# 2. Define a class Animal with a method make_sound that 
# prints "Some generic sound". Then define a class Dog that inherits 
# from Animal and overrides the make_sound method to print "Bark

'''class animal:
    def __init__(self):
        print("Some generic sound")
class dog(animal):
    def make_sound(self):
        print("Bark")      
dog=dog()
dog.make_sound()'''


# 4. Demonstrate multiple inheritance by creating classes Person and Employee, 
# where Employee inherits from Person. Then create another class Manager that 
    # inherits from both Employee and Leader.

class leader:
    def __init__(self):
        pass
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class employee(person):
    def __init__(self,name,age,emp_id):
        super().__init__()
        self.emp_id=emp_id
class manager(employee,leader):
    def __init__(self,name,age,emp_id):
        employee.__init__(self,name,age,emp_id)
        leader.__init__(self)
manager=manager("Bob",40,"E002")
print(manager.name,manager.age,manager.employee_id)



        
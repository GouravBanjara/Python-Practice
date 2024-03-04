# Static Method 
 
# class Math:
#     def __init__(self, num):
#         self.num = num

#     def addtonum(self, n):
#         self.num = self.num +n

#     @staticmethod #static method does not require self argument and it is not associated with the class but can be called if needed independently
#     def add(a, b):
#         return a+b

# a= Math(5)
# print(a.num)
# a.addtonum(6)
# print(a.num)

# print(Math.add(7,2))


# Instance Variables vs Class Variables
class Employee:
    companyName = 'Apple'  #this is a class variable which is set as default if instance variable is not given
    noOfEmployees = 0  #it is a class variable
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02 
        Employee.noOfEmployees +=1
    def showDetails(self):
        print(f'The name of the employee {self.noOfEmployees} is {self.name} and the raise amount in {self.companyName} is {self.raise_amount}' )

emp1 = Employee('Harry')
emp1.raise_amoun= 0.3  
emp1.companyName = 'Apple India'
emp1.showDetails()
Employee.companyName = 'Google' #here the instance companyName variable is given so it will override the class variable
print(Employee.companyName)

emp2 = Employee('Rohan')
# emp2.companyName = 'Nestle'
emp2.showDetails()

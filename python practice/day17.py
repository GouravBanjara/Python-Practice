# #Inheritance
# class Employee:
#      def __init__(self, name, id):
#           self.name = name
#           self.id = id

#      def showDetails(self):
#           print(f'The name of Employee: {self.id} is {self.name}')

# class Programmer(Employee):
#      def showLanguage(self):
#           print('The default language is Python')

# e1 = Employee('Rohan', 333)
# e1.showDetails()
# e2 = Programmer('Ajay', 123)
# e2.showDetails()                        



#Access Modifiers
class Employee:
    def __init__(self):
        self.__name = "Gourav" #the __ before name makes name variable unable to access directly this process is called name mangling 
    
a = Employee() 
# print(a.__name) #Cannot be accessed directly
print(a._Employee__name) #Can be accessed directly

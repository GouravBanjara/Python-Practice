# is vs '==' 
a = [1,2,43]
b = [1,2,43]
print(a is b) #'is' compares the location of objects 
print(a == b) #'==' compares the values of objects 



# Object Oriented Programming in Python (OOPs)

# Classes and Objects 
class Person:
    name = 'Gourav'
    occupation = 'Data Scientist'
    networth = 10
    def info(self):
        print(f'{self.name} is a {self.occupation}')

a = Person()
b = Person()
c = Person()

a.name = 'Shubham'
a.occupation = 'Accountant'

b.name = 'Nitika'
b.occupation = 'HR'

a.info()
b.info()
c.info()
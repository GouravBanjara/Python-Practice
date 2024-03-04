# Consttructors in Python
# class Person:
#      def __init__(self, name, occ):  # init method is called whenever a class object is created
#           print('Hey I am a Person')
#           self.name = name
#           self.occ = occ
#      def info(self):
#           print(f'{self.name} is a {self.occ}')

# a = Person('Gourav','Developer')
# b = Person('Hitesh', 'HR')
# a.info()
# b.info()


# Decorators in Python
def greet(fx):
     def mfx(*args, **kwargs):
        print('Good Morning')
        fx(*args, **kwargs)
        print('Thank you for using this function')
     return mfx
     

@greet   #every time add function is used greet will be called and it will decorate add function 
def add(a,b):
     print(a+b)

add(2,5)



    
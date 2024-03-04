# Getters and Setters
class MyClass:
    def __init__(self, values ):
        self.values = values
    
    def show(self):
        print(f'The value is{self.values}')
    
    @property #getter: returns the values of the argument after performing some calculations
    def ten_values(self):
        return 10*self.values

    @ten_values.setter
    def ten_values(self, new_values):
        self.values = new_values/10    

obj = MyClass(21)
obj.ten_values = 67
print(obj.ten_values)
obj.show()
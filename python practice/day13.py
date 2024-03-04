# lambda function
# def double(x): #the classic way to write a function 
#     return x*2

# double = lambda x: x*2 #same function but in a single line using lambda keyword 

# print(double(5))



# MAP 
# def cube(x):
#     return x*x*x 
# print(cube(2))

# l=[1,2,3,4,5,6] #suppose we need a cube of all these value in a list

# # newl = [] #the function method using for loop to get cube
# # for item in l:
# #     newl.append(cube(item)) 
            #OR
# newl = list(map(cube,l)) #the map method to find the cube of list values
            #OR
# newl = list(map(lambda x: x*x*x, l)) #the lambda way
# print (newl)

#FILTER
# def filter_function(a):
#     return a>4

# l=[1,2,3,4,5,6]
# newnewl = list(filter(filter_function,l)) #filter the values with the condition (here a>4)
# print(newnewl)



#Reduce
from functools import reduce

numbers = [1,2,3,4,5]

def mysum(x,y):  #calculate the sum of the numbers using teh reduce function
    return x+y

sum = reduce(mysum,numbers) #it will keep reducing the lenght of the list by adding them untill the final result 
print (sum)

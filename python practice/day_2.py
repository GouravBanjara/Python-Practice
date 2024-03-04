# # list
# marks = [2,4,5,6,5]
# print(type(marks))
# if 7 in marks:
#     print("Yes")
# else:
#     print("No")
# marks.append(7) #adding more values
# marks.sort(reverse=True) #sorting
# marks.reverse() #reverse the list values
# print(marks.index(5)) #index of the value
# print(marks.count(5)) #count the number of values in the list
# m=marks #it will reference the list and any changes in it will change the list
# m[0]=0
# n=marks.copy() #it will not change main list
# n[0] = 1
# marks.insert(1,22) #it will insert new value (22) on index(1) and the other values will shift
# g=[33,44,55]
# marks.extend(g) #extend the new list in main list
# print(marks)


# tuples #same as list but are immutable
# a=(5,8)
# print(type(a))
# print(a[0])


# exercise 1
# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# hour = int(timestamp)
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)

# if hour>0 and hour<12:
#     print("Good Morining")
# elif hour>=12 and hour<18:
#     print("Good afternoon")
# else:
#     print("Good evening")



# fstring
# letter  = "Hey my name is {} and i am from {}"
# country = 'India'
# name = 'Gourav'
# print(letter.format(name,country))
# print(f"Hey my name is {name} and i am from {country}") #by using f we can use variables


# doc string  
# def square(n):
#     '''Takes in a number, returns the square of n'''
#     print(n**2)
# square(5)
# print(square.__doc__) #won't ignore upper the msg and will be displayed


# recursions  
# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5))


# sets
# s = {2,3,3,4,5,6,6}
# print(s) # won't take any repeated values and order of values can vary and are immutable

# a = {} # it's an empty dictionary not an empty set
# b = set() #this is an empty set

# for values in s:
#     print(values)

# cities = {'Tokyo','Madrid','Berlin','Delhi'}
# cities2 = {'Tokyo','Seoul','Kabul','Madrid'}
# # cities3 = cities.union(cities2) #union will give the unique values
# # cities3 = cities.intersection(cities2) #intesection will give the common values
# # cities.intersection_update(cities2) #it will update the first set with common values of second set
# cities3 = cities.symmetric_difference(cities2) #it will give the uncommon values
# print(cities3) 

 

# dictionaries
# dic = {'harry':'Human Being', 'spoon':'object'}
# print(dic)
# print(dic.keys()) #will give only keys
# print(dic.values()) #will give only values
# for a in dic.keys():
#     print(dic[a])

# ep1 = {122:45, 123:89, 567:69, 670:69}
# ep2 = {222:67, 566:90}
# ep1.update(ep2) #update will add the two dictonaries into 1
# ep1.clear() #empty the dictionary
# ep1.pop(122) #remove the particular key value pair
# ep1.popitem() #it will remove the last key value pair
# del ep1 #it will delete the dictionary
# print(ep1)
# string slicing
# names = "Harry, Gourav"
# print(names[0:5])
# print(len(names))
# print(names[0:-3])
# print(names[-8:9])

# x = int(input("Enter the value of x: "))

# match x:
#     case 0:
#         print(x, 'is 0')
#     case 1:
#         print(x, 'is 1')
#     case _ if x>10:
#         print(x,'is neither 0 or 1 and is above 10')
#     case _:
#         print(x, 'is neither 0 or 1 and is below 10 ')


# for loop
# colors = ['Red','Green','Blue','Yellow']
# for a in colors:
#     print(" ")
#     for b in a:
#        print(b)


# while loop
# i=0
# while(i<3):
#     print(i)
#     i=i+1


# break, pass and continue statement
# for i in range(12):
#     if(i==10):
#         break #skip the code
#     print("5 x", i+1, "=", 5*(i+1))

# for b in range(12):
#     pass #does literally nothing

# for a in range(12):
#     if(i==10):
#         print("skip the iteration")
#         continue #skip the iteration
#     print("5 x", i, "=", 5*i)


# functions
# def gmean(a,b):
#     mean = (a*b)/(a+b)
#     print(mean)
# gmean(4,2)

# default arguments
# def avg(a=9, b=5):
#     print("the avg is ",(a+b)/2)
# avg(1,5) #override the default arguments

# keyword arguments
# avg(b=5, a=8) #changing the position of parameters

# required arguments
# def avg(a,b,c=2):
#     print(a+b+c)
# avg(3,5) #compulsory to give the undefined arguments

# variable length arguments
# def avg(*num):
#     sum=0
#     for i in num:
#         sum =sum+i
#     return sum/len(num)
# c= avg(5,6,7,8) #can put any length of numbers
# print(c)

# def name(**name): #same as above but data is in key value pair
#     print("Hello", name["fname"], name["mname"], name["lname"])
# name(mname="Honey", lname="Singh", fname="YO YO")






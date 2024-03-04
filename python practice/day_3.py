# for - else
# for i in range(6):
#     print(i)
#     # if i == 4:
#     #     break  #it will exit the for-else 
# else:  #it will end the loop successfully when all iterations are done 
#     print("Soory no i")


# for x in range(5):
#     print (f"iteration no {x +1} in for loop")
# else:
#     print('Out of loop')



# exception handling
# a = input("Enter the value:")
# print(f"Multiplication table of {a} is:")
# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# except ValueError: #can also defined the type of error
#     print("Enter only numerical values ")
# print('This program ran successfully')

# finally
# def func1():
#     try:
#         l=[1,5,6,7]
#         i=int(input("Enter the index: "))
#         print(l[i])
#         return 1
#     except:
#         print("some error occured")
#         return 0
#     finally: #it will execute the code even if we have returned the value in try-except block
#         print("I wiil be executed no matter what")
# x=func1()
# print(x)

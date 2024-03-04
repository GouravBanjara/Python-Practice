# short hand if-else
# a = 330
# b = 3303
# print("a") if a>b else print('=') if a==b else print('b') #this method makes readebility easy, starts with statement then condition 
# c=9 if a>b else 0
# print(c)  



# enumerate function: it allows us to keep track of our index in loop
# a = [12,56,32,98,45,12,1,4]
# for index, i in  enumerate (a):
#     print(index,'.', i)
#     if (index == 3):
#         print('Gourav, awesome')


# __name__ == '__main__'
def welcome():
    print("Hey Ho are you")

print(__name__) #it will only execute when i am running this code from this file only it won't run when i am importing this file somewhere
if __name__ == '__main__':
    welcome()


 
# return render_template("list.html",rows=rows)
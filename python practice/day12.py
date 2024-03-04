# read() readlines() and other methods
# f = open('file_handling_practice.txt','r')
# while True:
#     line = f.readline() #to read file line by line 
#     if not line: 
#         break
#     print (line)


# seek() tell() and other function
# with open('file_handling_practice.txt', 'r') as f:
#     print(type(f))
#     f.seek(10) #move to the 10th byte in the file
#     data = f.read(5) #read the next 5 bytes
#     print(f.tell()) #tells u the current position in the file
#     print(data)

# truncate()
with open('file_handling_practice.txt','a') as f:
    f.write('Hello ne world')
    f.truncate(40) #keep the byte size of the file tp 40
    


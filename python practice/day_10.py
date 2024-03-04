# langchain, prompt engineering, R language
# class central: free courses with certificate

# import day_9 #This method allows you to access only the code u  want from day_9 file

# day_9.welcome() 


# importing OS module 
import os

if(not os.path.exists("data")):
    os.mkdir("data")
 
# for i in range(1,10): #can make multiple folders
#     os.mkdir(f"data/day{i}")
    
# for i in range(1,10): #can remame multiple folders
#     os.rename(f"data/day{i}", f"data/File {i}")

folders = os.listdir("data") #provide all the content in a folder

print (folders)
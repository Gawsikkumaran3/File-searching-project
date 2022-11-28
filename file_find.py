import os
import re

#C drive path

os.chdir("C:/")
path = os.getcwd()

print("Your current directory is: "+ path)


def searchFile(filename):
    
    result = []
    result_type = []
    dir_list = os.listdir() 
    for file in dir_list:
        if file.lower() == filename.lower():
            result.append(file)
            if os.path.isfile(path+file): result_type.append("File: ")
            else: result_type.append("Directory: ")
            break
        elif re.search(filename.lower(),file.lower()):
            result.append(file)
            if os.path.isfile(path+file): result_type.append("File: ")
            else: result_type.append("Directory: ")
    else:
        if len(result)==0:
            result.append("Match not found")

    return result,result_type


filename = input("Enter the filename which you wanted to search: ")

output,output_type = searchFile(filename)

for x,y in zip(output,output_type):
    if x=="," and y==",":
        continue
    elif x=="Match not found":
        print(x)
    else:
        print(y,x)



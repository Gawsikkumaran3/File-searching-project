# File-searching-project

## Problem to solve

The program wants to find the specific file into current directory 

Hint : OS library

## Possible test cases

    - Getting the user input & searching the files based on the input filename

## Inputs

    - filename variable is to be created to get the input from the user

## Logic

import os
import re

print(os.getcwd())

def searchFile(filename):

    dir_list = os.listdir()

    for x in dir_list:
        if x == filename:
            result = os.getcwd+x
        elif re.search(filename,x):
            get_file_name = re.search(filename,x)
            result = get_file_name.string
        else:
            result = "Match not found"

    return result

filename = input("Enter the filename which you wanted to search ")
result = searchFile(filename)
print(result)

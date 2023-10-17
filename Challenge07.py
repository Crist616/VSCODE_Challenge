#!/usr/bin/python3
#Cristiano Garcia
#17/10/2023

# Import libraries

import os


# Declaration of variables
user_directory = input("Enter input: ")


# Declaration of functions
def walk_dir(path):
  
    for (root, dirs, files) in os.walk(path):
      print(root)
      print(dirs)
      print(files)

# Main 
walk_dir(user_directory)


# End
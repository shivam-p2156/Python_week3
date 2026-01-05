# Day 16 ------------------------------------>>>>>>

# Import in python 

import math 

a= math.sqrt(9)
print(a)


# Using from keyword 
from math import sqrt

b = sqrt(16)
print(b)

# Import everything
from math import *

c = sqrt(16)
print(c)

# Using as keyword

import math as m

d = m.sqrt(25)
print(d)

# DIR function 
print(dir(math))

"""
# ----------------- OS MODULE IN PYTHON ---------------

import os

# make directory
os.mkdir("abc")     

for i in range(0,5):
    os.mkdir(f"abc/day{i+1}")

# Current working directory
print("dir is ", os.getcwd())

# Change working directory 
print("dir is change ", os.chdir("/Users"))

# Lists of directory 
print(os.listdir("abc"))

# Check if path is exist
print(os.path.exists("abc"))

# Rename directory name
print(os.rename("abc","ABC"))

# Remove directory
os.rmdir("ABC")

for i in range(0,5):
    os.rmdir(f"ABC/day{i+1}")


"""
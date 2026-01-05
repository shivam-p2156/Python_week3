# Day 17 --------------------->>>>

# -------------- Local and Global variable -------------

var = 10 # This is Global variable

def func():
    var = 20 # This is Local variable
    print(var)

func()
print(var)

# Modifying Global variable with Local variable 

x = 5
def func1():
    global x
    x=50
    

func1()
print(x)
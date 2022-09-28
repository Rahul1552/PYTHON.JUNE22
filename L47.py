#################################################
#  22.08.2022 
#################################################
# TOPICS TO BE COVERED  
# MODULES IN PYTHON
#################################################


#################################################
# Modules
#################################################


print()
'''
collection of functions = Modules
collection of Modules = Package
collection of Packages = Library
Eg: print()
Eg: NumPy
Eg: Turtle
'''


#################################################
# Standard Python Libraries
#################################################


help(print())
print(dir(print())) # this will provide list of classes available in the module

print(dir()) # if no argument is given to dir()
print(dir(__builtins__)) # if no argument is given to dir()

# more readable format
# print(type(dir(__builtins__)))

# for i in dir(__builtins__):
#     print(i)



#################################################
# Standard Python Libraries
#################################################
# 1st Method 
import turtle

# print(dir(turtle))
# more readable format

# for i in dir(turtle):
#     print(i)
print("************ finding info about methods of the imported module********")
# print(dir(turtle.circle))
# printing square with circles on each corner
# turtle.forward(100)
# turtle.right(90)
# turtle.circle(30)
# turtle.forward(100)
# turtle.right(90)
# turtle.circle(30)

# turtle.forward(100)
# turtle.right(90)
# turtle.circle(30)

# turtle.forward(100)
# turtle.right(90)
# turtle.circle(30)


# turtle.done()


# 2nd method

from turtle import circle, back, done, forward
circle(50)
done()

# 3rd method

from turtle import * # star means everything
circle(50)
done()



# HW create a rectangle using turtle (use lengh = 100 , br = 30)
# ☝️ SHARE THE  OUTPUT SCREEN SHOT
#################################################
#  03.08.2022 
#################################################
# TOPICS TO BE COVERED  
# FUNCTIONS
#################################################

#################################################
# Python Lambda Functions
#################################################
# What are lambda functions in Python?
# In Python, an anonymous function is a function that is defined without a name.
# While normal functions are defined using the def keyword in Python, anonymous functions are defined using the lambda keyword.
# Hence, anonymous functions are also called lambda functions.

#################################################
# Syntax of Lambda Function in python
# lambda arguments: expression
# Lambda functions can have any number of arguments but only one expression.
#################################################



def sum1(x):
    z = x*3
    return z

ans  = sum1(4)
print(ans)

print(sum1(4))


print("**********using lambda ****************")

# Syntax 
# lambda arguments: expression

ans  = lambda x: x*3 # single argument 
print(ans(4))


ans  = lambda x,y,z: x*y*z # many arguments 
print(ans(2,8,4))

def larger(a,b):
    if a > b :
        print(a)
    else:
        print(b)

larger(0.41258,0.4789)


print("**********using lambda with if...else ****************")
larger  = lambda a ,b : a if (a > b) else b 
print(larger(0.41258,0.4789))




#################################################
# filter()
#################################################
print("********** filter function ****************")

list1 = [1,2,3,4,5,6,7,8,9]


for i in list1:
    if i%2 == 0:
        print(i)


print("**********filter function with lambda ****************")


# print(filter.__doc__) # to print info about the function

list2  = list(filter((lambda x :(x%2 == 0)),list1))
print(list2)
list2  = list(filter((lambda x :(x%3 == 0)),list1))
print(list2)


print("**********filter function without  lambda ****************")
# HW check with normal in place of lambda
list1 = [1,2,3,4,5,6,7,8,9]

def one(x):
    if x%2 == 0: 
        return True


# we should not use () while calling the function 
list2  = list(filter(one(),list1))
print(list2)

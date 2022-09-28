#################################################
#  04.08.2022 
#################################################
# TOPICS TO BE COVERED  
# FUNCTIONS
#################################################




#################################################
# map()
#################################################
# this is used to map
# to create pair 


# from functools import reduce


# print("**********map  function with  lambda ****************")

# list3 = [1,2,3,4,5,6,7,8,9]

# a = []
# for i in list3:
#     i = i * 2
#     a.append(i)
#     # print(i)
# print(a)


# print(map.__doc__) #dunder doc

# #Syntax for map()
# # map(func, *iterables) 


# a = list(map((lambda x: x * 2),list3))

# print(a)


# print("**********map  function with  lambda  for square****************")

# b = list(map((lambda x : x ** 2) , list3))
# print(b)

# # google 

# #################################################
# # reduce()
# #################################################



# print(reduce.__doc__)



#################################################
# TOPICS TO BE COVERED  
# Exceptions
#################################################

#################################################
# Exception handling  in Python
# https://docs.python.org/3/library/exceptions.html#exception-hierarchy
#################################################
# Que : Error Vs exception  ?


#  code block

# Syntax for try..except

'''
try:
    code under lens , doubtful code
except:
    print(" Explain the code error)
'''

# a = b/c # the code will break at this line , if not handled properly


# try:
#     a = b/c
# except:
#     print(" Some Error occured")

# print(3+5)




# #################################################
# getting help in python
# #################################################


# help(Exception)


# #################################################
# particular Exception
# #################################################


print("********** Exception for the programmer to check in testing phase****************")


# try:
#     a = b/c
# except Exception as e:
#     print(e)

print(3+5)



print("**********handling particular Exception****************")
try:
    b = 33 # defining b to remove name error 
    c = 0 # assign non zero value to remove  ZeroDivisionError
    a = b/c

except NameError:
    print(" define the value of b ") # this is for end user 

except ZeroDivisionError:
    print(" the value of c cant be Zero ") # this is for end user 

print(3+5)


print("**********particular Exception for the End user ****************")
try:
    b = 33 # defining b to remove name error 
    c = 0 # assign non zero value to remove  ZeroDivisionError
    a = b/c

except NameError:
    print(" define the value of b ") # this is for end user 

except ZeroDivisionError:
    print(" the value of c cant be Zero ") # this is for end user 

print(3+5)
#################################################
#  23.07.2022 
#################################################
# TOPICS TO BE COVERED  
# 👉 FLOW CONTROL IN PYTHON Contd.
#################################################
#################################################
# membership condition
#################################################

# CHECKING MEMBERSHIP IN  sets, tuple , dict membership ??


set1  = {1,2,3,4,5}

if 7 in set1:
    print("Element is present")
else:
    print("Element is absent  present")

# key : values 


dict1  = {
    1 : "First",
    2 : "Second",
    4 : "Forth"
}

if "two" in dict1:
    print("Element is present")
else:
    print("Element is absent  present")



if 2 in dict1:
    print("Element is present")
else:
    print("Element is absent  present")




#################################################
# TRUTHY VALUES
# https://docs.python.org/3/library/stdtypes.html#truth-value-testing
#################################################


# Falsy Values Includes:
# 1) Sequences and Collections:
# Empty lists []
# Empty tuples ()
# Empty dictionaries {}
# Empty sets set()
# Empty strings ” “
# Empty ranges range(0)
# 2) Numbers: Zero of any numeric type.
# Integer: 0
# Float: 0.0
# Complex: 0j
# 3) Constants:
# None
# False

print(True)
print(type(True))
print("True")
print(type("True"))



print(False)
print("False")

#SYNTAX
    # if <conditions> :
        # <block of code>


# conditions > always in boolean


if 1 :
    print("I am inside IF ")
else:
    print("I am inside ELSE ")


if 0:
    print("I am inside IF ")
else:
    print("I am inside ELSE ")

print("************************")

if [1,2,3] :
    print("I am inside IF ")
else:
    print("I am inside ELSE ")


if {1,2,3,4,5} :
    print("I am inside IF ")
else:
    print("I am inside ELSE ")



if 0 :
    print("I am inside IF ") #this code is not reachable
else:
    print("I am inside ELSE ")


print("*********Checing with  -1***************")


if -1 : # bool value of neg num is True
    print("I am inside IF ") #this code is not reachable
else:
    print("I am inside ELSE ")




# #########################################
# Loops
    # for
    # while 
# #########################################

#for loop
# syntax 
    # for <variable> in <some iterable>:
        #do something /print/compare
        # block of code

print("*********FOR LOOP************")


name1 = "Minkole"

for i in name1:
    print(i)


list1  = [2,4,6,8,10]

for j in list1:
    print(j)



















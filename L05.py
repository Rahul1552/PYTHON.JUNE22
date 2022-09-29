#################################################
# Day 06  : 28.06.2022
#################################################
# TOPICS TO BE COVERED 
# 👉 VARIABLES IN PYTHON 
#################################################

'''
aLLOWED variables Eg: 
iam
i_am
_iam
_i_am
I_AM
I_am
i_am_no1
no1_1_am
1_i_am # not valid variable name
'''
# over writing a variable by different values !!!

i_am = 1
print(i_am)

i_am = 100
print(i_am)

i_am = "MinSkole"
print(i_am)


# One value to multiple variables :

i_am = "Indian"
you_are = "Indian"
we_are = "Indian"


print(i_am)
print(you_are)
print(we_are)

#writing in one line 

i_am = you_are = we_are = "Indian"
print("************printing in one line ************")
print(i_am)
print(you_are)
print(we_are)


i_am = you_are = we_are = 400076
print(i_am)
print(you_are)
print(we_are)


# many values to Multiple variables in one line 
print("************manny values to Multiple variables in one line ************")
i_am ,you_are ,we_are = "Person1" ,"Person2","Person3"
# i_am ,you_are ,we_are = "Person1" ,"Person2"
print("I_am is:" ,i_am)
print("you_are:" ,you_are)
print("we_are is:" ,we_are)



print(i_am) # latest value assigned in the variable 

# Memory ref/address if the values assgned is same
print("************Memory ref/address************")

i_am = you_are = we_are = "Indian"
print("I_am:" ,i_am)
print("you_are:" ,you_are)
print("we_are :" ,we_are)


print("************Memory address output are as below ************")
print(id(i_am))
print(id(you_are))
print(id(we_are))

# the other memory address remains unchanged 
i_am = "Indian1"
print(id(i_am))
print(id(you_are))
print(id(we_are))

#################################################
#  22.07.2022 
#################################################
# TOPICS TO BE COVERED  
# 👉 FLOW CONTROL IN PYTHON Contd.
#################################################



# Logical operators
#  AND , OR ,NOT 
# Identity operators
#  IS , NOT IS 
# Membership operators
# IN , NOT IN 



#SYNTAX
    # if <conditions> :
        # <block of code>

#################################################
# checking the eligibility of driving
#################################################

# HOW TO CHECK MULTIPLE CONDITIONS
# checking multiple conditions using Logical operators 
    # AND OR NOT


age  = int(input("Enter your age:"))
dl = input("Enter if you have DL : y/n :")
work_ex = int(input("Enter your work experience:"))
ola_employee_id =input("Are you ola_employee : y/n :")
ola_owner = input("Are you ola_owner : y/n :") 


# =  assignment operator , to assign the value 
# === comparison , to compare values

# FIRST MEHTHOD

if age >= 18 and dl =="y" and work_ex >=2 or ola_employee_id == "y" :
    print("You can apply")
else:
    print("You can not  apply")


# SECOND MEHTHOD

if age >= 18 and dl =="y" and work_ex >=2 :
    print("You can apply")

elif ola_employee_id == "y" :
    print("You can apply")


elif ola_owner == "y" :
    print("You can apply")

else:
    print("You can not  apply")


# HOW MANY  ".ELIF.." CAN BE USED BETWEEN  >>> IF ... ELSE 

'''
if <condition>

elif <condition>

elif <condition>

elif <condition>
.
.
.
else:
    block of code

'''



#################################################
#  MEMBERSHIP operator IN  ,NOT IN
#################################################

# CHECKING MEMBERSHIP IN STRING
name1  = "MinSkole"


if "m" in name1.casefold(): # case sensitive
    print(name1.casefold())
    print("Y")
else:
    print("N")

# CHECKING MEMBERSHIP IN  LIST

# print(set("abcdef"))

list_fruits  = ['e', 'd', 'f', 'b', 'a', 'c']

if "d1" in list_fruits:
    print("Fruit is present")
else:
    print("Fruit is absent ")

# CHECKING MEMBERSHIP IN  sets, tuple , dict membership ??



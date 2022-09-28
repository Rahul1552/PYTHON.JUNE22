#################################################
#  21.07.2022 
#################################################
# TOPICS TO BE COVERED  
# 👉 FLOW CONTROL IN PYTHON
#################################################



# COMPARISON
# LOGICAL
# MEMBERSHIP


'''
Python supports the usual comparison conditions from mathematics:
Equals:                     a == b
Not Equals:                 a != b
Less than:                  a < b
Less than or equal to:      a <= b
Greater than:               a > b
Greater than or equal to:   a >= b
'''


# Logical operators
#  AND , OR ,NOT 
# Identity operators
#  IS , NOT IS 
# Membership operators
# IN , NOT IN 



# BLOCK OF CODE

# 
###########################################
# If statements 
# #########################################


#SYNTAX
    # if <conditions> :
        # <block of code>


a  = 100

if a == 100:
    print("Yo have scored century !!!! congrats")

# checking if  the studenT has passed the exam , if grand_total > 150  !!!

# p = int(input("Enter your Marks in p :")) 
# c = int(input("Enter your Marks in c :"))
# m = int(input("Enter your Marks in m :"))


# grand_total  =  p+c+m
# print(f"Your grand_total is {grand_total}")

# if grand_total > 150 :
#     print("You have passed the exam ! Congrats !!!")
# else:
#     print("Sorry !!! you have failed")


# VOTING AGE 

voter_age = int(input("Please enter your age : "))


if 18 <= voter_age <=64:
    print("You are eligible to vote !!!")
    print("Use your Voting power properly")


elif 65 < voter_age <=100: 
    print("You are eligible to vote !!!")
    print("You can ask the staff for help !!!")


else:
    print("You not are eligible to vote !!!")
    print("Please wait for {} years".format(18- voter_age))










































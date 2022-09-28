#################################################
#  26.07.2022 
#################################################
# TOPICS TO BE COVERED  
# Loops
    # for
    # while 
#################################################

list_even = [2,4,6,8]
for i in range(0,11,2):
    # print(i,end=" ")
    print(i)



#################################################
#  use of range()
#################################################

# sum of first 10 number
print("sum of first 10 number")
sum1 = 0
for i in range(11):
    sum1  = sum1 + i
print(sum1)


#################################################
#  nested for loop
#################################################

# # mult tables 
# for i in range(1,11):
#     for j in range(1,11):
#         # print("Mul table of  {0} is {1} ".format(i , i*j))
#         print("Mul table  {0} * {1} is {2} ".format(i,j , i*j))
#         # hw print the above using f-string 


# for i in range(1,11):
#     for j in range(1,11):
#         for k in range(1,11):
#             print(i*j*k)


###################################
# WHILE LOOP
###################################
# Python While Loop is used to execute a block of statements repeatedly 
# until a given condition is satisfied.
# indefinite iteration.
'''
Syntax: 
while expression:
    statement(s)
'''


i = 0
while i < 5:
    print("I will attend classes ")
    i = i+ 1
    print(i)
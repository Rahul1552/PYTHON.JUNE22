#################################################
#  28.07.2022 
#################################################
# TOPICS TO BE COVERED  
# while LOOP
#################################################
'''
Syntax: 
while expression:
    statement(s)
'''
################################################
#  ASKING USER TO QUIT THE GAME 
#################################################

# a = int(input("Press -1 to quit the Game "))

# while a != -1:
#     a = int(input("Press -1 to quit the Game "))

# print("Good Bye !!!")


################################################
# guessing game !!!
################################################

# ans  =  int(input(" Guess the number !!!"))

# while ans != 5 :
#     ans = int(input(" Guess the number !!!"))

# print("You have guessd it right !!!")

# # Add HINT code in the guessing game 


################################################
# COMPARING WHILE VS IF LOOP !!!
################################################

# print("using for")
# for i in range(1,11):
#     print(i)


# print("using while")

# i = 1
# while i < 11:
#     print(i)
#     i = i +1 


################################################
# BREAK , CONTINUE , PASS
################################################


print("using BREAK")

i = 1
while i < 11:
    print(i)
    if i == 5: # code will exit at 5 
        break 
    i = i +1
    



print("using CONTINUE")
i = 0
while i < 11:
    
    i = i +1
    if i == 5: # 5 will be skipped and code will contiue 
        continue 
    print(i)
    

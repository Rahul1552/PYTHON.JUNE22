
#################################################
#  29.07.2022 
#################################################
# TOPICS TO BE COVERED  
# FUNCTIONS
#################################################

# 3 REPEAT
# why ? to avoid duplication of code  , avoid repeating 


# syntax
# def fun_user_defined():
#     block of code



#################################################
# The pass Statement
#################################################


def greeting():
    pass


greeting()


#################################################
# not recommended to use in other area like in loops
#################################################
# print("using pass")

# i = 1
# while i < 11:
#     pass # THE LOOP WILL WAIT FOR THE CODE BLOCING FURTHER CODES




#################################################
# CREATING USER DEFINED FUNCTION
#################################################


def greeting():
    print("Welcome to Minskole")
    print(" We are Online")
    pass
    print(" We are Online again")

greeting()


def multiply5():
    print(5*5*5)


multiply5()

def multiply6():
    print(6*6*6)

multiply6()



def multiply7():
    print(7*7*7)

multiply7()


# using parameters 

def multiply(a): # here a is called parameter
    print(a*a*a)

multiply(8) # value of a i.e 8 is call argument 

def greeting1(text):
    print("Welcome to " +  text)


# calling the function

greeting1("Mumbai")
greeting1("Pune")

#################################################
# Parameters vs Arguments 
#################################################

#when some value is assigned to a paramter , it is called argument

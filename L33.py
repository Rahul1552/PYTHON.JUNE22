#################################################
#  02.08.2022 
#################################################
# TOPICS TO BE COVERED  
# FUNCTIONS
#################################################

#################################################
# LIST as input 
#################################################

list1 = [1,2,3,4,5,6]
list2 = (1,2,3,4,5,6)
dict1 = {
    1: "first",
    2: "Second",
    3: "Third"

}

def roll_num(x):
    for i in x:
        print(i)
print("***************list as input **********")
roll_num(list1) # list
print("***************tuple as input **********")
roll_num(list2) # tuple
print("***************dict  as input **********")
roll_num(dict1) # dict



# HW check for sets 



#################################################
# return values 
#################################################


print("***************return values  **********")
def multiply1(x,y):
    z = x*y
    # print(z)
    return z

ans  = multiply1(5,8)
print(ans)


a = multiply1(2,1)
print(a)
b = multiply1(2,2)
print(b)
c = multiply1(2,3)
print(c)
d = multiply1(2,4)
print(d)


print("***************return values with for loop **********")
for i in range(1,11):
    table_two = multiply1(2,i)
    print(table_two)



#################################################
# Documentation using "Docstring"
#################################################

# Document your code 
# PEP 257 – Docstring Conventions
# https://peps.python.org/pep-0257/


print("***************Docstring **********")
def multiply1(x,y):
    '''
    This is for multiplying two numbers
    Input as two integers 
    output as complex conversion 
    NOTE: Dont use three numbers
    '''

    z = x*y
    # print(z)
    return z

# ans  = multiply1(5,8)
# print(ans)

print(multiply1.__doc__) # checking for user defined

print(print.__doc__) # for the inbuilt using 
# double underscore =  dunder doc

print(len.__doc__)
print(range.__doc__)


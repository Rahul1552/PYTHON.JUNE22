#################################################
#  06.08.2022 
#################################################
# TOPICS TO BE COVERED  
# File  handling/operations  in Python
# https://docs.python.org/3/library/exceptions.html#exception-hierarchy
#################################################



# #################################################
# Raising an  Exception ( cont from  Exception class)
# #################################################


x = int(input("Enter Even number"))
if x % 2 !=0:
     raise Exception("Enter only Even number")
else:
     print("You have enterd:" + x)

num = int(input("Enter   number only "))

if not type(num) is int:
     raise Exception("Enter only integer")
else:
    print("Your ans is :" + str(num))


def div1(a,b):
    if b == 0:
        raise ZeroDivisionError("You have entered Zero as deno , Enter another non zero num")
    else:
        c = a/b
        return c 

ans  = div1(15, 5)
print(ans)



#####################################
# Python File I/O
#####################################
'''
a file operation takes place in the following order:
1. Open a file
2. Read or write (perform operation)
3. Close the file # resources that are tied with the file are freed.
'''



# x = [1,2,3,4,5,6,7,8,9,10]

# for i in x :
#     print(i)


#####################################
# Opening  files in Python 
#####################################


'''
Files :
1 . Binary
2 . Text file
'''

file = open(r"C:\Users\RAHUL\Documents\OnePython\good_day.txt")
text = file.read()
print(text)
file = open(r"C:\Users\RAHUL\Documents\OnePython\Preamble.txt")
text = file.read()
print(text)

# realtive path vs absolute path ?






















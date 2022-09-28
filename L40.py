#################################################
#  13.08.2022 
#################################################
# TOPICS TO BE COVERED  
# File  handling/operations  in Python
#################################################



#################################################
# appending the file 
#################################################



print("************ appending the file  ******************")

f = open(r"C:\Users\RAHUL\Documents\OnePython\2.JUNE_22\CLASS\roll_num.txt" ,"a")
f.write("\n This is no five  file") # overwrite the file 
print(f.mode)
f.close()
print(f.closed)




#################################################
# using content manager
#################################################

print("************ using content manager ******************")

with open(r"C:\Users\RAHUL\Documents\OnePython\2.JUNE_22\CLASS\roll_num.txt" ,"a") as f:
    f.write("\n This is no six  file") # overwrite the file 
    print(f.mode)
    print(f.closed)

print(f.closed) # outside with 


#################################################
# reading a file using for loop
#################################################

with open(r"C:\Users\RAHUL\Documents\OnePython\2.JUNE_22\CLASS\roll_num.txt" , "r") as f:
    for line in f:
        print(line)



#################################################
# HW
# reading a file using while loop
# truthy values !!!
#################################################

# HW write above code using while loop

print("************ using while loop ******************")

with open(r"C:\Users\RAHUL\Documents\OnePython\2.JUNE_22\CLASS\roll_num.txt") as f:
    data = f.readline()
    # INITIALIZING THE VARIABLE
    # PRINTING THE FIRST LINE 
    while data:
    # WHILE <EXPRESSION>
        data = f.readline()
        print(data)




#################################################
# JSON
#################################################

'''
JSON is a syntax for storing and exchanging data.
JSON is text, written with JavaScript object notation.
Python has a built-in package called json, which can be used to work with JSON data.
'''


print("************ using JSON loads ******************")

import json

x =  '{ "Name":"MinSkole", "PinCode":440012, "city":"Pune"}'# looks like  Python dict but is in JSON format
print(type(x))

y = json.loads(x) # converting json into dict in Python
print(type(y))
print(y)


print("************ using JSON dumps ******************")

z = json.dumps(y) # z will be a string after conversion

print(type(z))
print(z)

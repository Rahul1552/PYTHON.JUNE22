#################################################
#  02.07.2022
#################################################
# TOPICS TO BE COVERED 
# 👉 METHODS AVAILABLE IN STRINGS 
# https://docs.python.org/3/library/stdtypes.html#string-methods
#################################################

# what are methods
# methods vs function

#################################################
# len()
#################################################
string1  = "India is my Country"
print(len(string1))

string2  = "India@75 Now"
print(len(string2))

string2  = '''India@75
Now'''
print(len(string2)) # enter will also be counted as a character



#################################################
# upper()
#################################################

name1 = "Rahul Singh"
print(name1.upper()) # all upper case


#################################################
# lower()
#################################################

name1 = "RAHUL SINGH"
print(name1.lower()) # all lower case

#################################################
# strip()
#################################################

string3 = " The space in start and at the end     "
print(string3)
print(string3.strip())

#################################################
# split()
#################################################

email1 = "grahulsingh2020@gmail.com"
x = email1.split("@") # the output will be in the form of list
print(x)
print(type(x))
print(x[0]) # getting 1st element from the list



#################################################
# casefold()
#################################################

name1 = "Rahul Singh"
print(name1.lower()) # all lower case
print(name1.casefold()) # all in small case

name3  = input("Enter your Name :")
print(name3.casefold()) # to convert to lower case before comparing 


#HW 
# run the below code and 
# compare the difference in the output
# also try other methods available in the official docs
#################################################

thought = 'Life is like riding a bicycle. To keep your balance, you must keep moving.'

print(len(thought))
print(thought)


print(thought.capitalize())
print(thought.casefold())
print(thought.lower())
print(thought.upper())
print(thought.title())




#################################################
#  casefold() vs lower()
#################################################
'''
str.casefold()
Return a casefolded copy of the string. 
Casefolded strings may be used for caseless matching.

Casefolding is similar to lowercasing but more aggressive 
because it is intended to remove all case distinctions in a string. 
For example, the German lowercase letter 'ß' is equivalent to "ss". 
Since it is already lowercase, lower() would do nothing to 'ß'; 
casefold() converts it to "ss".

'''
# simple words  : use lower() if end user is only using English
# simple words  : use casefold() if end user's language is unknown

#################################################
# operators 
#################################################

# using operators 
# in ,not in

print(len(string1))
string2 = "India is my country"
print(len(string2))
print("India" in string2)
print("my" in string2)
print("My" not in string2)



#################################################
# Day 05  : 27.06.2022
#################################################
# TOPICS TO BE COVERED 
# 👉 ESCAPE CHARACTER
# 👉 Comment - Single line  , Multi Line , raw string
#################################################
# ESCAPE SEQUENCE


# Escape Character Meaning
# \”                Double quote
# \’                Single quote
# \\                backslash
# \n                New line
# \r                Carriage Return
# \t                Horizontal tab
# \b                Backspace
# \f                form feed
# \v                vertical tab
# \0                Null character
# \N{name}          Unicode Character Database named Lookup
# \uxxxxxxxx        Unicode Character with 16-bit hex value XXXX
# \Uxxxxxxxx        Unicode Character with 32-bit hex value XXXXXXXX
# \ooo              Character with octal value OOO
# \xhh              Character with hex value HH


# to print in tab
student1  = " The Students in the class are  \tRahul \tImran \tPallavi  "
print(student1) # one tab = 4 space

fav1 = " My fav nos are 5\t10\t15\t20\t25"
print(fav1)

# to print in new line 
student1  = " The Students in the class are  \nRahul \nImran \nPallavi  "
print(student1) 


# using single quotes ''

print( 'Hello World') #single
print( "Hello World") # double
print( '''Hello World''') # triple

# DOUBLE   quotes ""
# print('Hey , I 'll see you tomorrow')
print("Hey , I 'll see you tomorrow")


# using TRIPLE quotes ''' '''
# print("Ramesh said "I will work hard for the Project")
print('''Ramesh said "I will work hard for the Project''')


# comments in python is done  through HASH
# another way to comment  is through multi line comments using ''''''

# eg :  using hash
# name is Rahul
# this is line 1 of address
# this is line 2 of address
# this is line 3 of address
# this is line 4 of address
# pin = 400076

# eg: comment using ''' '''

'''
name is Rahul
this is line 1 of address
this is line 2 of address
this is line 3 of address
this is line 4 of address
pin = 400076
'''


# to ignore new  line i.e enter in the output
student1  = ''' The Students in the class are   as below : \
Rahul  \
Imran  \
Pallavi  '''

# The Students in the class are     Rahul   Imran   Pallavi
print(student1) 

#multi line output using  triple quotes ''' '''

address1 = '''
name is Rahul \
this is line 1 of address \
this is line 2 of address \
this is line 3 of address \
this is line 4 of address \
pin = 400076
'''


print(address1)
#################################################
# RAW STRING
#################################################
# raw string  as an alternate way for Escape character 

print(r"C:\Users\RAHUL\Documents\OnePython\2.JUNE_22\CLASS") # not recomm
print(R"C:\Users\RAHUL\Documents\OnePython\2.JUNE_22\CLASS") # not recomm
print("C:\\Users\RAHUL\Documents\OnePython\\2.JUNE_22\CLASS") # recomm


# HW 
# 1.  output should be as below 
# 2.  output should be in a single line 

# shcool_addres = 
# desired output as below 👇!
# Name of Institution   VIDYA NIKETAN SCHOOL
# Affiliation Number    1130428
# State MAHARASHTRA
# District  CHANDRAPUR
# Postal Address    DADAWADI PARISAR,
# NAGPUR ROAD, 
# CHANDRAPUR, 
# MAHARASHTRA
# Pin Code  442401

#################################################
#  01.07.2022
#################################################
# TOPICS TO BE COVERED 
# 👉 BUILT-IN DATA TYPE OF PYTHON: STRINGS
# 👉 SLICING
# 👉 BUILT-IN METHODS THAT YOU CAN USE ON STRINGS.
# 👉 .foramt and f-string for printing
#################################################

#################################################
#  STRINGS
#################################################

# what is a string 
# ''
# ""
# '''


string1 = 'Hello World'
print(type(string1))

'''

INDEX POSITION 	0	1	2	3	4	5	6	7	8	9	10
CHARACTER	    H	e	l	l	o		W	o	r	l	d

'''

print(string1)

# accessing each character in the string 

print(string1[6])
print(string1[0])
print(string1[5])
print(string1[3])
print(string1[10])


#################################################
#  SLICING OF STRINGS
#################################################


# print(string1[start : End]) syntax , always n-1 is the END
print(string1[6:10])
print(string1[6:11])

print(string1[0:5])
print(string1[0:11])
print(string1[5:6]) # this will print only one char 
print("*******when either of the start or end value is not given*******")
# when either of the start or end value is not given
# it will be either of default START or END value
print(string1[0:]) # END value if not given then by default last value +1 will be used
print(string1[:11]) # START value if not given then by default "0" will be used

print(string1[:])


#################################################
#  SLICING OF STRINGS
#################################################

# HHW
 
'''
INDEX POSITION 	0	1	2	3	4	5	6	7	8	9	10	11	12
CHARACTER	I		L	O	V	E		P	Y	T	H	O	N

'''

# USE SLICING TO GET THE BELOW OUTPUTS

"I"

"LOVE"

"PYTHON"

"VE PY"

"I LO"

"HON"

"I LOVE PYTHON"


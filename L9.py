#################################################
#  02.07.2022
#################################################
# TOPICS TO BE COVERED 
# 👉 SLICING
#################################################


#################################################
# SLICING OF  STRINGS WITH NEGATIVE INDEXING 
#################################################

'''
INDEX POSITION 	0	1	2	3	4	5	6	7	8	9	10
CHARACTER	    H	e	l	l	o		W	o	r	l	d
	        -11   -10	-9	-8	-7	-6	-5	-4	-3	-2	-1

'''

string2 = "Hello World"

print(string2[-1])
print(string2[-7])
print(string2[-11])
print(string2[-6])

# slicing 
print(string2[-11:-6])
print(string2[-11:5])
print(string2[-11:9])
print(string2[-11:-1])
print(string2[-11:0])
print(string2[-11:1])

# if one of the values are missing 

print(string2[-11:])
print(string2[:])

# jump string 

# SYNTAX FOR JUMP/STEP VALUES 
# print(string2[START: END : STEP])

print(string2[-11::1])
print(string2[-11::2])
print(string2[-11::3])

# HW with positive indexing : step  values

# revesing the string/ sentence using negative step value

print(string2[::-1])

#################################################
# HW to  understand slicing with steps/jump value
#################################################

# step values in positive indexing

thought = " PRACTICE MAKES A MAN/WOMAN PERFECT"
print(len(thought)) # len is 35

print(thought[0:20:2])
print(thought[0:20:3])
print(thought[0:20:1])
print(thought[0:32:1])
print(thought[0::1])

# step values in negative indexing

print(thought[0:-20:2])
print(thought[-33:-25:3])
print(thought[0:-17:1])
print("************")
print(thought[0:-32:1])
print(thought[0::-1])
print(thought[::-1])


























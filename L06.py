#################################################
# Day 07  : 29.06.2022
#################################################
#  TOPICS TO BE COVERED 
# 👉 INTRO BUILT-IN DATA TYPE OF PYTHON:
# 👉  TYPE CASTING  PYTHON:
#################################################

'''
Text Type			: str
Numeric Types		: int, float, complex
Sequence Types		: string ,list, tuple, range
Mapping Type		: dict
Set Types			: set, frozenset
Boolean Type		: bool
Binary Types		        : bytes, bytearray, memoryview
None Type			: NoneType
'''


# INTRO TO BUILT IN DATA TYPES 

i_am = 1
# how to get data type in python ????
print(type(i_am))

i_am = 100
print(type(i_am))

i_am = 1.11 # decimal will be float
print(type(i_am))

i_am = 3.1417
print(type(i_am))

i_am = -3.1417
print(type(i_am))


i_am = -0.000123
print(type(i_am))


i_am = 1+2j
print(type(i_am))

# i_am = 1+2i # the complex part should be "j" only 
print(type(i_am))


print("*********Strings**********")

i_am = "r"
print(type(i_am))
i_am = "Rahul"
print(type(i_am))
i_am = "Rahul is learning Python 3.10"
print(type(i_am))



print("*********List**********")
i_am_list = [1,2,3,4,5]
print(type(i_am_list))
i_am_list = ["r" ,"a" ,"h", "u","l"]
print(i_am_list)
print(type(i_am_list))

i_am_list =[1,2,3,4,5,"r" ,"a" ,"h", "u","l"] # list can contain different data types
print(i_am_list)
print(type(i_am_list))


print("*********dictionary**********")

i_am_dict = {
    "r" : "Rahul",
    "a": "Amar",
    "c" : "Chetana"
}
print(type(i_am_dict))


i_am_dict = {
    "r" : 1,
    "a": 2,
    "c" : 3
}
print(type(i_am_dict))

i_am_dict = {"r" : "Rahul","a": "Amar","c" : "Chetana"}
print(type(i_am_dict))



# HW 
i_am_string = ""
iam_list = []
i_am_dict = {}

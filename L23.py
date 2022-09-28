#################################################
#  20.07.2022 
#################################################
# TOPICS TO BE COVERED  
# 👉 METHODS IN A DICTIONARY
# Changed in version 3.7: Dictionary order is guaranteed to be insertion order
#  Changed in version 3.8: Dictionary views are now reversible
#################################################


a = ("Nirmal",33.4)
b = ("Nizamabad",54.6)
c = ("Jagtial",35.9)
d = ("Peddapalli",36)
e = ("Jayashankar",30.8)

# using basic way
rainf = dict()
print(rainf)

rainf = {
    "Mumbai" : 25.9,
    "Pune" : 22.4
}
print(rainf)

# using dict method 

rainf = dict([a,b,c,d,e])
print(rainf)








#################################################
#updating  a dict
#################################################

a = ("Nirmal",22.6)
b = ("Nizamabad",54.6)
c = ("Jagtial",35.9)
d = ("Peddapalli",36)
e = ("Jayashankar",30.8)
rainf = dict([a,b,c,d,e])


rainf = dict([a,b,c,d,e])
rainf["Nirmal"] = 220

print(rainf)

rainf.update({"Nirmal" : 500})
print(rainf)

rainf["Nirmal"] = ""
print(rainf)


rainf["Nirmal"] = None
print(rainf)


rainf["Nirmal"] = True
print(rainf)

# #################################################
# # removing items from dict
# #################################################

rainf.pop("Nirmal")
print(rainf)

rainf.popitem() # remove the last element  = ctrl+z , undo
print(rainf)


rainf.pop("Peddapalli")
print(rainf)

# clearing the dict

# rainf.clear()
# print(rainf)

# del rainf # deleted the dict
# print(rainf) # this will give error



# #################################################
# copy
# #################################################

rainf2 = rainf

rainf2["Nirmal"] = None
print(rainf2)
print("***original***********")
print(rainf)


print(id(rainf))
print(id(rainf2))

rainf3 = rainf.copy()
print(id(rainf3))
rainf3["Nirmal"] = ""
print(rainf3)
print(rainf)


# #################################################
# ways of creating a dictionary
# https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
# #################################################


a = dict(one=1, two=2, three=3) # string are not in quotes
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'one': 1, 'three': 3}, two=2)
# print(a == b == c == d == e == f)


# sets | order = no | values should be same in any oreder
# list ??


list1  = [1,2,3,4]
list2  = [2,3,4,1]

set1 =set(list1)
set2 =set(list2)

print(list1 == list2)
print(set1 == set2)







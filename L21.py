#################################################
#  18.07.2022
#################################################
# TOPICS TO BE COVERED  
# 👉 DICTIONARY
# 👉 METHODS IN A DICTIONARY
#################################################


# What are Dictionaries ???
# we use sets to build Dictionaries 
#should not use "dict" = class
# curly braces |  sets 


dict1 = {
    #key : values pair 
    #roll no : student name
    #key has to be unique

    1 : "one",
    2 : "two",
    3 : "three"
}


print(dict1)



dict2 = {1 : "one " , 2 :"two" , 3 : "three"}
print(dict2)


#################################################
# accessing elements in the dictionary
#################################################

#indexing ?
#ordered ??
# mutable ??

print(dict1[1])
print(dict1[2])
print(dict1[3])
# print(dict1[4])

# using get() to access the value

print("*using get() to access the value*")
print(dict1.get(1))
print(dict1.get(2))
print(dict1.get(3))
print(dict1.get(4)) # for undefined key the op will be None

# code will not break with .get()
# code will be faster with  [] 



# accessing the keys 

print("**** accessing the keys******")

print(dict1.keys())
a = dict1.keys()

print(type(a))

print("**** accessing the values******")


print(dict1.values())

# mapping to be discussed tomorrow 


print("**** accessing both keys and values******")


print(dict1.items())
print(type(dict1.items()))

print(type(1))
print(type("One"))









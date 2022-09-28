#################################################
#  14.07.2022
#################################################
# TOPICS TO BE COVERED  
# 👉 TUPLES Contd.
# 👉 SETS
#################################################


# #########################################
# packing/unpacking  a Tuple
# #########################################

print("*******Packing**************")
tuple1 = (2,4,6,8)
print(type(tuple1))
print(tuple1)
print(tuple1[1])
print(tuple1[2])

print("*******Normal way **************")
a = tuple1[0]
b = tuple1[1]
c = tuple1[2]
d = tuple1[3] 

print(a)
print(b)
print(c)
print("*******unpacking **************")

a,b,c,d = tuple1

print(a)
print(b)
print(c)


print("******unpacking of a List***************")



list007 = [107,207,307,407]

a ,b ,c,d = list007

print(a)
print(b)
print(c)
print(d)


# #########################################
# Sets
# #########################################
# unordered 
# no indexing 
# slicing not possible 

print("******Sets**************")

set1 = {1,3,5,7,11,13,17,19} # set of prime numbers

print(set1)
print(set1[0]) # unordered so this  will give error








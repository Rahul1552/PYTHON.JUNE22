#################################################
#  19.07.2022
#################################################
# TOPICS TO BE COVERED  
# 👉 PROPERTIES OF A DICTIONARY
# 👉 METHODS IN A DICTIONARY
#################################################


# verifying the Properties of a Dict with examples


# creating an EMPTY Dictionary using dict()

dict_rank = dict()
print(type(dict_rank))
print(dict_rank)

# filling  a dictionary


dict_rank = dict({1 : "First" , 2: "Second"})
print(dict_rank)

# using tuple

print("**********using tuple for initialising a dictionary ***********")

a  = (1, " First")
b  = (2, "Second")
c  = (3 , "Third")
d  = (4 , "Forth")

dict_rank = dict([c, d, a , b ])
print(dict_rank)

dict_rank = dict([a , b , c ,d ])
print(dict_rank)


dict_rank = dict([b , c ,d , a ])
print(dict_rank)



print("**********checking for duplicity ***********")

dict_rank = dict([a , b , c ,d , a, c])
print(dict_rank)

a  = (1, " F")
dict_rank = dict([a , b , c ,d ,a]) # updated the value
print(dict_rank)


print("**********comparing ways of representing a dict ***********")

dict_rank = {
    1 : "First",
    2 : " Second",
    3 : "Third",
    4 : "Forth"
}
print(dict_rank)


print(dict_rank)
dict_rank = dict([a , b ,c, d ])
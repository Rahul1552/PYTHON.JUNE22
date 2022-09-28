#################################################
#  12.07.2022
#################################################
# 👉 METHODS IN LISTS ( CONTINUED)
# 👉 TUPLES
#################################################



# #########################################
# reverse()
# #########################################


list_alpha= ["w","f","r","t","d","v","F"]


list_alpha.sort(reverse=True) # in reverse order of the item 
print(list_alpha)

list_alpha.reverse()  # reverse the indexing order
print(list_alpha)

list1 = [ [56, 98],[1,3] , [5,4] ,[5,24]]
list1.reverse()
print(list1)


list3 = [ [5,4] ,[5,24] ,["a","d"]] # only index position is relevent 
list3.reverse()
print(list3)




# #########################################
# making  a copy 
# #########################################

print("making a copy")
list_alpha1 = ["w","f","r","t","d","v","F"]

list_alpha2 =  list_alpha1.copy()

print(list_alpha1)
print(id(list_alpha1))

print(list_alpha2)
print(id(list_alpha2))









# #########################################
#  Tuples 
# #########################################
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.


capital_states= ("Bhopal","Mumbai","Imphal","Shillong","Aizawl","Kohima")

print(type(capital_states))

print(capital_states[3])
print(capital_states[2])
print(capital_states[0])
print(capital_states[-1])


capital_states[0] = "Hyderabad"

print(capital_states)





















# #########################################
# access same as string or a list
# #########################################














# #########################################
#  Tuples are unchangeable, or immutable 
#  we have to convert it into list 
#  before modifying
# #########################################




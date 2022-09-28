#################################################
#  11.07.2022
#################################################
# TOPICS TO BE COVERED 
# 👉  2 METHODS IN LISTS
#################################################

#################################################
#  remove()
#################################################

clean_cities= ["Indore","Surat","Vijaywada","Navi Mumbai","Pune","Raipur","Bhopal","Vadodara"]

print(type(clean_cities))
print(len(clean_cities))

clean_cities.remove("Vadodara")
print(clean_cities)



#################################################
#  pop()
#################################################



clean_cities.pop(0)
print(clean_cities)

clean_cities.pop(4)
print(clean_cities)


clean_cities.pop(4)
print(clean_cities)

print("Using neg indexing")
clean_cities.pop(-1)
print(clean_cities)





#################################################
#  clear()
#################################################

clean_cities.clear()
print(clean_cities) # empty list 




#################################################
#  del()
#################################################

del clean_cities
# print(clean_cities) # empty list 


#################################################
#  sort()
#################################################

list4 = [2,4,3,5,66,34,55,2,9]
list4.sort() # ascending order 
print(list4)


list4.sort(reverse=True) # descending order
print(list4)



list_alpha= ["w","f","r","t","d","v","F"]

list_alpha.sort()
print(list_alpha)

list_alpha.sort(reverse=True) # in reverse order
print(list_alpha)

list_alpha.sort(key=str.lower) #not case sensitive
print(list_alpha)


#################################################
#  nested lit
#################################################


print("Nested Listed")
list1 = [ [56, 98],[1,3] , [5,4] ,[5,24]]
list1.sort()
print(list1)



list_num1 = [["z,x"],["p,d"],["s,r"],["t,w"]]
list_num1.sort()
print(list_num1)
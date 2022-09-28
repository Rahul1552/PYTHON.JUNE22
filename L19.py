#################################################
#  15.07.2022
#################################################
# TOPICS TO BE COVERED  
# 👉 TUPLES Contd. | repeat class
# 👉 METHODS IN SETS
#################################################


#################################################
#  ON SET ELEMENTS 
#################################################

 

#################################################
#  add
#################################################

set1 = {3,6,9,12,15}
set1.add(18)

set1.add(21)
set1.add("MinSkole")
# set1.add([5,10,15,20]) #TypeError: unhashable type: 'list'
# set1.add({5,10,15,20}) # TypeError: unhashable type: 'set'
# set1.add((5,10,15,20)) #TypeError: unhashable type: 'set'
# print(set1)



#################################################
#  update
#################################################
set3 = {3,6,9,12,15}
print(len(set3))

set4 = {4,8,12,16}
print(len(set4))
set3.update(set4)

print(set3)
print(len(set3))

#################################################
#  remove
#################################################
set3 = {0,3,6,9,12,15}
print(set3)
set3.remove(0)
print(set3)
# set3.remove(10) # this will throw error if the element is missing 
# print(set3)


#################################################
#  discard
#################################################


print("**********using discard*********")
set3 = {0,3,6,9,12,15}
set3.discard(100) # this will not throw error evne if the element is missing 
set3.discard(15) # this will not throw error evne if the element is missing 
print(set3)



#################################################
#  pop
#################################################
set3 = {0,3,6,9,12,15}
set3.pop() # no argument has to be given
print(set3)
set3.pop() # no argument has to be given
print(set3)
set3.pop() # no argument has to be given
print(set3)

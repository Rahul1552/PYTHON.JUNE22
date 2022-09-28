#################################################
#  08.07.2022
#################################################
# TOPICS TO BE COVERED 
# 👉 METHODS IN LISTS
#################################################



#################################################
#  insert()
#################################################

banks_India = ["HDFC Bank",
"State Bank of India",
"ICICI Bank",
"Axis Bank",
"Kotak Mahindra Bank",
"IndusInd Bank",
"Yes Bank",
"Punjab National Bank"]


banks_India.insert(6 ,"UCO Bank") # at a particular position
print(banks_India)
banks_India.insert(6 ,["UCO Bank1" ,"UCO Bank2"])
print(banks_India)

# banks_India.insert("Canara Bank") # position is compulsory
# print(banks_India)

#################################################
#  append()
#################################################


banks_India.append("Tata bank") # at the end of the list
print(banks_India)


#################################################
#  extend()
#################################################
odd1 = [1,3,5,7,9]
even1 = [2,4,6,8] 
# a = odd1.extend(even) # the output will be None
# print(a)

odd1.extend(even1)
print(odd1)

# extending with different data types !!!

student1_roll = [1,2,3]
print(type(student1_roll))
student1_name = {
    1:"a",
    2: "b",
    3:"c"}
print(type(student1_name))

student1_roll.extend(student1_name)
print(student1_roll)

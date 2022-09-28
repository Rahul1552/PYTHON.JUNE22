#################################################
#  16.07.2022
#################################################
# TOPICS TO BE COVERED  
# 👉 MATHEMATICAL OPERATIONS ON SETS
# 👉 TYPE CASTING
#################################################

e = {0,2,4,6,8,10}
o = {0,1,3,5,7,9}
o1 ={3,5}

print(e.intersection(o))
print(e.union(o))
print(e.difference(o))
print(e.symmetric_difference(o))
print(o1.issubset(o))


#################################################
# TYPE CASTING
#################################################

# num1 = int(input("Enter your lucky number :"))
# print(num1)
# print(type(num1))


s = "MinSkoole"

print(type(s))
print(set(s))
print(type(s))

print(set(["Minskole","Pune",400076]))
print(set({"Name" : "Minskole",
"Addr" :"Pune", 
"Pin": 400076})) # to store the keys 


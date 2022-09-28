#################################################
# Day 09  : 30.06.2022
#################################################
# TOPICS TO BE COVERED 
# 👉 BUILT-IN DATA TYPE OF PYTHON: STRINGS
# 👉 TYPECASTING
#################################################


'''
done so far 
Numbers
String 
List
Dict
'''


# set and bool/boolean


print("*********sets**********")

set1  = {1,3,5,9,11,13,15} # set of odd numbers
print(set1)
print(type(set1))

set1  = {1,3,5,9,"r","a"} # set of odd numbers
print(set1)
print(type(set1))


# set1  = {1,3,5,9,[2,4,6,8,10]} #TypeError: unhashable type: 'list'
# print(set1)
# print(type(set1))

print("*********booleans**********")

#booleans 
# True /False

x = True
print(x)
print(type(x))


z = False
print(z)
print(type(z))

print("*********trick questions**********")

x = 5
print(x)
print(type(x))

# nothing
i_am_what = ""
print(i_am_what)
print(type(i_am_what))

i_am_what = " "
print(i_am_what)
print(type(i_am_what))


i_am_what = []
print(i_am_what)
print(type(i_am_what))

i_am_what = {}
print(i_am_what)
print(type(i_am_what))

# spaces
i_am_what = { }
print(i_am_what)
print(type(i_am_what))


i_am_what = '1'
print(i_am_what)
print(type(i_am_what))

i_am_what = [1]
print(i_am_what)
print(type(i_am_what))

i_am_what = {1} #type = set , no key : value pair 
print(i_am_what)
print(type(i_am_what))

# commas

i_am_what = [1]
print(i_am_what)
print(type(i_am_what))


i_am_what = [1,]
print(i_am_what)
print(type(i_am_what))



i_am_what = (7,) # check o/p
print(i_am_what)
print(type(i_am_what))


i_am_what = (7)
print(i_am_what)
print(type(i_am_what))



i_am_what = {25}
print(i_am_what)
print(type(i_am_what))



i_am_what = {"R"}
print(i_am_what)
print(type(i_am_what))


i_am_what = {50,}
print(i_am_what)
print(type(i_am_what))


i_am_what = {"name" :"MinSkole"}
print(i_am_what)
print(type(i_am_what))

#################################################
# type casting
#################################################
# conversion of one data  type to another
print("*********type casting**********")

# display1 = input("Enter your age in Numbers:")
# print(type(display1))
# # final1 = int(display1)
# # print(final1)

s1 = "Thirty five " #35
s2 = "35" # can be converted


x = 1.2
print(type(x))

z = int(x)
print(z)


y = 35
print(float(y))

num1 = "35"
print("Before conversion")
print(type(num1))
print("After conversion")

num2 = int(num1)
print(num2)
print(type(num2))


# i_am_what = {:}
# print(i_am_what)
# print(type(i_am_what))


display1 = input("Enter your age in Numbers:")
print(type(display1))
final1 = int(display1)
print(final1)
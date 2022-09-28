#################################################
#  06.07.2022
#################################################
# TOPICS TO BE COVERED 
# 👉 STRINGS FORMATTING 
# 👉 LISTS
#################################################



#################################################
# Formatting string using format() method 
# 1. Default
# 2. Positional 
# 3. Keyword based 
# https://docs.python.org/3.4/library/string.html
#################################################
a = 10
b = 20
c = a + b


print(c)
print("The sum of", a ,"and", b ,"is :",  c) # can take any number of arguments 
print("The sum of {} and {} is :{}".format(a ,b , c)) #Default
print("The sum of {0} and {1} is :{2}".format(a ,b , c)) #Positional
print("The sum of {1} and {0} is :{2}".format(a ,b , c))   #Positional


fname= input("Enter your First name")
sname= input("Enter your Surname name")

print("Good morning", fname , sname)
print("Name  first")
print("Good morning {} {}".format(fname,sname)) #Default
print("Surname first ")
print("Good morning {1} {0}".format(fname,sname)) #Positional

# print("The sum of {a} and {b} is :{c}".format(a = 100,b=200,c=a+b)) 
# # only valuse can be assigned to the key , operations will give error

print("The sum of {a} and {b} is :{c}".format(a = 100,b=200,c=300)) #Keyword based 



#################################################
# f string method
#################################################

a = 90
b = 10
c = a + b
print("The sum of", a ,"and", b ,"is :",  c) 
print(f"The sum of {a} and {b} is : {c}") 



#################################################
# HW use built in methods to solve below questions
# 1. count how many times the word "Jaya" appeared
# 2. replace "Bhaarat" with "India"
# share the ouput screenshot
#################################################


song2 = '''
Jana Gana Mana Adhinaayak Jaya Hey, 
Bhaarat Bhaagya Vidhaataa 
Panjaab Sindhu Gujarat Maraatha, 
Draavid Utkal Banga 
Vindhya Himaachal Yamuna Ganga, 
Uchchhal Jaladhi Taranga
Tav Shubh Naamey Jaagey, 
Tav Shubh Aashish Maange Gaahey 
Tav Jayagaathaa 
Jana Gana Mangal Daayak, Jaya Hey Bhaarat Bhaagya Vidhaataa 
Jaya Hey, 
Jaya Hey, 
Jaya Hey, 
Jaya Jaya Jaya, 
Jaya Hey
'''


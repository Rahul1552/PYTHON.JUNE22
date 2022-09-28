#################################################
#  05.07.2022
#################################################
# TOPICS TO BE COVERED 
# 👉 METHODS AVAILABLE IN STRINGS (Contd.)
# 👉 MEMBERSHIP OPERATOR
# https://docs.python.org/3/library/stdtypes.html#string-methods
#################################################


#################################################
# replacing the string using replace()
#################################################
name1 = "Rahul R Singh"
print(name1)

print(name1.replace("R" , "RR"))

print(name1.replace(" " , "@"))

#################################################
# count and find
#################################################

a = "I will   learn Python3 , I promise !!! "
print(a.count("I")) # total no of appearence 
print(a.find("I")) # index of 1st appearence 
print(a.count("will")) # index of 1st appearence 
print(a.find("will")) # index of 1st appearence 



#################################################
# is+condition use
# isalpha
# isnumeric
# isalnum
# isspace
#################################################


code1  = "ZAQ!2wsx"
print(code1.isalpha()) # exclusively alphabets should be there

code2  = "Password"
print(code2.isalpha()) # output will be boolean 

code3 = "Pass123"
a= code3.isalnum()
print(a)


code5 = "MinSkole Pune"
print(code5.isspace()) #exclusively SPACE should be there


code6 = " "
print(code6.isspace())


#################################################
# operators  > Membership
#################################################

# using operators 
# in ,not in


string2 = "India is my country"
print(len(string2))
print("India" in string2) # is the given string present 
print("my" in string2)
# using casefold in combination with membership operator
print("india" not in string2.casefold())



#################################################
# HW use built in methods to solve below questions
# 1. count how many times the word "Tera" appeared
# 2. replace "Tera" with "Mera"
# share the ouput screenshot
#################################################


song1= '''
Dil Ki Surkh Deewaron Pe
Dil Ki Surkh Deewaron Pe
Deewaron Pe
Naam Hain Tera Tera
Naam Hain Tera Tera
Naam Hain Tera Tera
Naam Hain Tera Tera
Naam Hain Tera Tera
Naam Hain tera tera
Naam Hain tera tera
Naam Hain Tera Tera
'''


print("*******replacing tera --------- mera***********")
print(song1.casefold().replace("tera","mera"))


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


# counting the "Jaya"
print(song2.casefold().count("jaya"))

# replaing "Bhaarat" with "India"

print(song2.replace("Bhaarat" , "India"))
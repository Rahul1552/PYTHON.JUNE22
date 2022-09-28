#################################################
#  07.07.2022
#################################################
# TOPICS TO BE COVERED 
# 👉 LISTS
#################################################


# #########################################
# understanding Lists in detail 
# #########################################

'''
"HDFC Bank",	        0
"State Bank of India",	1
"ICICI Bank",	        2
"Axis Bank",	        3
"Kotak Mahindra Bank",	4
"IndusInd Bank",	    5
"Yes Bank",         	6
"Punjab National Bank"	7
'''


banks_India = ["HDFC Bank",
"State Bank of India",
"ICICI Bank",
"Axis Bank",
"Kotak Mahindra Bank",
"IndusInd Bank",
"Yes Bank",
"Punjab National Bank"]



print(banks_India)
print(type(banks_India))

print(" The 1st Bank is : {}".format(banks_India[0]))
print(" The 3rd Bank is : {}".format(banks_India[2]))
print(" The 7th Bank is : {}".format(banks_India[6]))
print("The lenght is : ")
print(len(banks_India))
print(" The 8th Bank is : {}".format(banks_India[7]))
print(" The last Bank is : {}".format(banks_India[-1]))


print(" The top 3 Banks are : {}".format(banks_India[0:3]))
print(" TheJump Banks are : {}".format(banks_India[0:7:2]))


# #########################################
# understanding Lists in detail 
# #########################################

# REPLACING ITEMS IN THE LIST WITH ITEM
banks_India[6] ="bandhan bank"
print(banks_India)


# REPLACING ITEMS IN THE LIST WITH LIST
banks_India[6] =["bandhan bank", "UCO Bank"]
print(banks_India)






































# #########################################
#  Modifying the List
# #########################################
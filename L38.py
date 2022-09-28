#################################################
#  09.08.2022 
#################################################
# TOPICS TO BE COVERED  
# File  handling/operations  in Python
#################################################
'''
1. TEXT = PLAIN TEXT
2. JSON = FOR INTERNET USE
3. CSV =  HANDLING SPREADSHEETS 
4. Binary = FOR IMAGES,MP3 ETC
'''


#####################################
# Python File I/O
#####################################
'''
a file operation takes place in the following order:
1. Open a file
2. Read or write (perform operation)
3. Close the file # resources that are tied with the file are freed.
'''

#################################################
# • Reading from a text file
#################################################
#################################################
# • Using read, readline, readlines
#################################################


print("************Using read******************")


f = open(r"C:\Users\RAHUL\Documents\OnePython\2.JUNE_22\CLASS\Preamble.txt") # f is pointer here , opening the file
data  = f.read()  # reading and storing in a variable
print(data) # printing the output
f.close()



f = open(r"C:\Users\RAHUL\Documents\OnePython\2.JUNE_22\CLASS\HarGharTiranga.txt.txt")
data = f.read()
print(data)
f.close()
print(f.closed) # status of the file


print("************Using read with argument in the fun******************")
f = open(r"C:\Users\RAHUL\Documents\OnePython\2.JUNE_22\CLASS\HarGharTiranga.txt.txt")
data = f.read(15)
print(data)
f.close()
print(f.closed) # status of the file



print("************Using readline with argument ******************")
# this will read line by line 
# iterate over a file 


f = open(r"C:\Users\RAHUL\Documents\OnePython\2.JUNE_22\CLASS\HarGharTiranga.txt.txt")
data = f.readline(15)
print(data)
data = f.readline() # read from 16th characte in the next command 
print(data)
data = f.readline()
print(data)
data = f.readline()
print(data)
data = f.readline()
print(data)
f.close()




print("************Using readlines ******************")
# saves the file contents in the form of list
# so we can apply all the properties and methods of a list


f = open(r"C:\Users\RAHUL\Documents\OnePython\2.JUNE_22\CLASS\HarGharTiranga.txt.txt")
data = f.readlines()
print(data)
print(type(data))
f.close()



print("************Using readlines ******************")
f = open(r"C:\Users\RAHUL\Documents\OnePython\2.JUNE_22\CLASS\Preamble.txt")
data = f.readlines()
print(data)
f.close()




print("************Using readlines ******************")
f = open(r"C:\Users\RAHUL\Documents\OnePython\2.JUNE_22\CLASS\roll_num.txt")
data = f.readlines()
print(data)
print(type(data))
print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])
f.close()


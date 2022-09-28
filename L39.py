#################################################
#  10.08.2022 
#################################################
# TOPICS TO BE COVERED  
# File  handling/operations  in Python
#################################################



#################################################
'''
1. TEXT = PLAIN TEXT
2. JSON = FOR INTERNET USE
3. CSV =  HANDLING SPREADSHEETS 
4. Binary = FOR IMAGES,MP3 ETC
'''
#################################################

'''
a file operation takes place in the following order:
1. Open a file
2. Read or write (perform operation)
3. Close the file # resources that are tied with the file are freed.
'''

# print("************Using read******************")

# f = open(r"C:\Users\RAHUL\Documents\OnePython\2.JUNE_22\CLASS\Preamble.txt") # raw string  = r 
# data  = f.read()
# print(data)
# print(f.closed) # to cehck if the file is open or closed state
# f.close()
# print(f.closed)


'''
read() # noraml reading 
readline() # one line at a time 
readlines() # converts the file into a list format 

'''


# print("************Using readline ******************")
# f = open(r"C:\Users\RAHUL\Documents\OnePython\2.JUNE_22\CLASS\Preamble.txt") # raw string  = r 
# data  = f.readline()
# print(data)
# data  = f.readline()
# print(data)
# data  = f.readline()
# print(data)
# data  = f.readline()
# print(data)



# print("************Using readlines******************")

# f = open(r"C:\Users\RAHUL\Documents\OnePython\2.JUNE_22\CLASS\Preamble.txt") # raw string  = r 
# data  = f.readlines()
# # print(data)
# # print(data[0])
# # print(data[10])
# print(data[::-1])
# print(type(data))



print("************ writing in a file ******************")

# f = open(r"C:\Users\RAHUL\Documents\OnePython\2.JUNE_22\CLASS\Preamble.txt") 
# data  = f.read()
# print(data)
# f.close
# print(f.closed)
# print(f.mode)

# syntax for arguments inside the open()
# open(" name of file / path " ," mode of operation : default = read" , "encoding type  defauls = OS dependent")




# f = open("Preamble.txt")      # equivalent to 'r' or 'rt'
# f = open("Preamble.txt",'w')  # write in text mode
# # f = open("img.bmp",'r+b') # read and write in binary mode



'''

Mode  Description
r     Opens a file for reading. (default)
w     Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
x     Opens a file for exclusive creation. If the file already exists, the operation fails.
a     Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
t     Opens in text mode. (default)
b     Opens in binary mode.
+     Opens a file for updating (reading and writing)
f = open("Preamble.txt")      # equivalent to 'r' or 'rt'
f = open("Preamble.txt",'w')  # write in text mode
f = open("img.bmp",'r+b') # read and write in binary mode
Unlike other languages, the character a does not imply the number 97 until it is encoded using ASCII (or other equivalent encodings).
Moreover, the default encoding is platform dependent. In windows, it is cp1252 but utf-8 in Linux.
So, we must not also rely on the default encoding or else our code will behave differently in different platforms.
Hence, when working with files in text mode, it is highly recommended to specify the encoding type.
f = open("Preamble.txt", mode='r', encoding='utf-8')
'''




print("************ writing in a file ******************")



f = open(r"C:\Users\RAHUL\Documents\OnePython\2.JUNE_22\CLASS\roll_num.txt" ,"w")
f.write(" This is no two  file") # overwrite the file 
print(f.mode)
f.close()
print(f.closed)

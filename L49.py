#################################################
#  24.08.2022 
#################################################
# TOPICS TO BE COVERED  
# OS MODULES IN PYTHON
# https://docs.python.org/3/library/os.html#module-os
# https://docs.python.org/3/library/datetime.html#module-datetime
#################################################

import os 

# help(os)

# for i in dir(os):
#     print(i)


# present/current working directory

# print(os.getcwd())

# chnging cwd
os.chdir(r"C:\Users\RAHUL\Documents\CAPF 2020")
# print(os.getcwd())

#listing dir

# print(os.listdir())
# print(type(os.listdir()))

# for i in os.listdir():
#     print(i)

#creating dir


# os.mkdir("wow2")
# print(os.getcwd())
# os.chdir(r"C:\Users\RAHUL\Documents\CAPF 2020")
# print(os.getcwd())


# for i in range(1,51):
#     os.mkdir("wow{}".format(i))


# deleting dir

# os.rmdir("wow1")
# os.rmdir("wow3")
# os.rmdir("wow4")


# creating sub dir
# os.makedirs("wow51/how51/yes51")

# os.removedirs("wow51/how51/yes51") # not recommended , risky

# renaming a dir 

# os.rename("wow5", "wow95")

#getting info about the dir i.e metadata
print(os.stat("wow95").st_size)
# print(type(os.stat("wow95")))
# help(os.stat_result)




















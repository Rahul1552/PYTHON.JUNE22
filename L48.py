#################################################
#  23.08.2022 
#################################################
# TOPICS TO BE COVERED  
# MODULES IN PYTHON
#################################################



#################################################
# TIME MODULE
#################################################


import time

# how to get help for time modules

help(time)
for i in dir(time):
    print(i)

# HW 
# what is daylight savings


# how to get time
print(time.time())

# o/p 1661258647.5252004 # what is this value = seconds passed since 1st jan 1970
# Epoch = 1st jan 1970
 
print(time.gmtime(0))
print(time.localtime())


print(time.time())

print(type(time.gmtime()))
help(time.struct_time)


print(time.localtime(time.time()))

# # converting into more readable format usng asctime

print(time.asctime(time.localtime(time.time())))




#################################################
# to calculate the execution time 
#################################################


start_time = time.time() # capturing start time 
print(start_time)

sum =0

for i in range(2000000):
    sum+=1


time.sleep(5)
end_time   = time.time() #capturing end time

exe_time = end_time - start_time
print("The time taken for execution is :" , exe_time)


print("********using  process_time to calculate the time spend by CPU*******")


start_time = time.process_time() # capturing start time 
print(start_time)

sum =0

for i in range(2000000):
    sum+=1
time.sleep(5) # the execution time will not be impacted because of this 5 second sleep

end_time   = time.process_time() #capturing end time

exe_time = end_time - start_time
print("The time taken for execution is :" , exe_time)



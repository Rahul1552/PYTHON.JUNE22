#################################################
#  25.07.2022 
#################################################
# TOPICS TO BE COVERED  
# 👉 FLOW CONTROL IN PYTHON Contd.
#################################################

# #########################################
# Loops
    # for
    # while 
# #########################################


#for loop
# syntax 
    # for <variable> in <some iterable>:
        #do something /print/compare
        # block of code

print("*********FOR LOOP************")

# to print elements in a dicionarY

d = {
    1 : "First",
    2 : "Second",
    3 : "Third",
    5 : "Fifth"
}



for i in d :
    print(i)
#     print(i,d[i])

print("************ using _ ")

for _ in d : # using _ is noot recommended 
    print(_)
    # print(i,d[_])


# ###################################
# # range is a sequence !!!
# ###################################

# # https://docs.python.org/3/library/stdtypes.html#typesseq
# # There are three basic sequence types: lists, tuples, and range objects
# # range is not a function



print(list(range(10)))


# a = 100
# a = pow (1000, 1000)


print(list(range(10)))

print(list(range(1, 11)))

print(list(range(0, 30, 5)))

print(list(range(0, 10, 3)))

print(list(range(0, -10, -1)))

print(list(range(0)))

print(list(range(1, 0)))


print("************ for loop with range()*************")


for i in range(10):
    print(i)



for i in range(10):
    print("*"*i)

#################################################
#  01.08.2022 
#################################################
# TOPICS TO BE COVERED  
# FUNCTIONS
#################################################

#################################################
# TYPES OF VARIABLE SCOPE
#################################################

print("*********Local Scope******")

a = 10

def mul():
    a =9 #1st preference 
    z = a * a
    print(z)
    print(id(a))

mul()
print(id(a))

print("*********Global  Scope******")

a = 10

def mul():
    global a
    a  = 100 
    z = a * a
    print(z)
    print(id(a))

mul()
print(a)
print(id(a))


print("*********Global  Scope 2nd Example ******")

#  step 1 :  check locally inside the function  
#  step 2 :  check ouside  the function  i.e globally

z = 5
print(z)
z = 10
print(z)
print(id(z))


def banner():
    global z
    # z = 55
    print(z)
    print(id(z))

banner()
print(z)
print(id(z))

print("*********Global  Scope extension to another function ******")

z = 5


def banner():
    global z
    z = 55
    print(z)
    print(id(z))

def banner2():
    # z = 555
    print(z)
    # print(id(z))


banner2()
banner()

# use of global keyword is bad practise in Python !!!....
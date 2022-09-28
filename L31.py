
#################################################
#  31.07.2022 
#################################################
# TOPICS TO BE COVERED  
# FUNCTIONS
#################################################



#################################################
# SCOPE OF A VARIABLE
#################################################

a = 35 # scope = GLOBAL

def multiply():
    a  = 5 * 6 # scope = LOCAL
    print(a)

print(a) # 1st 35
multiply() # 2nd  30 # not overwrite
print(a) #  3rd  35


b = a  + 10 # global value will be used 
print(b)


def cube1(a):
    cube = a*a*a
    print(cube)

cube1(5)

# HW how to access global variable inside a function ??

#################################################
# default values 
#################################################


def banner (text="Welcome to our City"):
    print(text)


banner("Welcome to Pune")
banner()
banner("Welcome to Nasik")
banner()


#################################################
# MORE ABOUT PARAMTER
#################################################

print("**********MORE ABOUT PARAMTER ***********")
# no parameter
def banner1():
    print(" WELCOME TO NO PARAMTER")

banner1()

# single  parameter
def banner2(text):
    print(text)

banner2(" With Single Parameter")


# single  parameter with default value 
def banner3(text="Welcome to our City"):
    print(text)

banner3(" With Single Parameter and default value")

banner3()

# multiple parameters

def banner4(greeting , name ): # POSITIONAL ARGUMENT
    print(greeting + name)
    print(name  + greeting)

banner4("Good Morning " , "Monali")
banner4( "Monali  " , "Good Morning " )
banner4(name="Monali  " , greeting="Good Morning " )


def div(x,y):
    z= x/y
    print(z)

div(30,10)
div(10,30)
div(0,20)
div(y=20,x=0) # KEYWORD ARGUMENT 

































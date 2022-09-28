#################################################
#  05.08.2022 
#################################################
# TOPICS TO BE COVERED  
# Exception handling  in Python
# https://docs.python.org/3/library/exceptions.html#exception-hierarchy
#################################################

'''
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- EncodingWarning
           +-- ResourceWarning
'''


# #################################################
# particular Exception
# #################################################



print("********** during development phase for identifying the expected Errors ****************")

# ValueError
# ZeroDivisionError

# try:
#      a = int(input("Enter the First Num : "))
#      b = int(input("Enter the Second  Num : "))
#      c = int(input("Enter the Third  Num : "))
#      ans  = b +c
#      print(ans)
#      z = ans/a
# except Exception as error:
#      print(error)

# print(" The code flow is ok ")


# print("********** for end user to understand what is the error in simple language****************")

# try:
#      a = int(input("Enter the First Num : "))
#      b = int(input("Enter the Second  Num : "))
#      c = int(input("Enter the Third  Num : "))

# except ZeroDivisionError:
#      print("You cant divide by Zero , enter corret number  ")
# except ValueError:
#      print(" Use numbers in Figures  eg:1 , 3")

# print(" The code flow is ok ")






# print("********** using else block with try...except ****************")

# try:
#      a = int(input("Enter the First Num : "))
#      b = int(input("Enter the Second  Num : "))
#      c = int(input("Enter the Third  Num : "))

# except ZeroDivisionError:
#      print("You cant divide by Zero , enter corret number  ")
# except ValueError:
#      print(" Use numbers in Figures  eg:1 , 3")
# else: # IF THE CODE IS ERROR FREE USE CODE UNEDR THE ELSE BLOCK 
#      ans  = b +c
#      print(ans)
#      z = ans/a
#      print(z)


# print(" The code flow is ok ")


print("********** using finally   with  try...except ****************")

try:
     a = int(input("Enter the First Num : "))
     b = int(input("Enter the Second  Num : "))
     c = int(input("Enter the Third  Num : "))
     ans  = b +c
     z = ans/a

except ZeroDivisionError:
     print("You cant divide by Zero , enter corret number  ")
except ValueError:
     print(" Use numbers in Figures  eg:1 , 3")
else: # IF THE CODE IS ERROR FREE USE CODE UNEDR THE ELSE BLOCK 
     
     print(ans)
     print(z)

finally:# irrespective of success of above code 
     print(" The code flow is ok ")




# #################################################
# Raising an  Exception
# #################################################


x = int(input("Enter Even number"))
if x % 2 !=0:
     raise Exception("Enter only Even number")
else:
     print("You have enterd:" + x)

num = int(input("Enter   number only "))

if not type(num) is int:
     raise Exception("Enter only integer")
else:
    print("Your ans is :" + str(num))


def div1(a,b):
    if b == 0:
        raise ZeroDivisionError("You have entered Zero as deno , Enter another non zero num")
    else:
        c = a/b
        return c 

ans  = div1(15, 5)
print(ans)
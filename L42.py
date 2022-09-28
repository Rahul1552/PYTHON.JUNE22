#################################################
#  17.08.2022 
#################################################
# TOPICS TO BE COVERED  
# OOP OBJECT ORIENTED PROGRAMMING
#################################################
# TEMPLATE
# BLUEPRINT





#################################################
# SYNTAX OF A CLASS
#################################################

class NameOfClass(): # name should be in CamelCase

    def __init__(self,param1,param2): #dunder methods > dunder init > constructor ?
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        # to perform some action
        print(self.param1)



#################################################
# user defined objects using class
#################################################


class Sample_new():
    pass # to define the class later , we use pass


my_class = Sample_new()

print(type(my_class))
# op is : <class '__main__.Sample'>

z = 3.0
print(type(z))


#################################################
# creating attributes (property. behaviour) : variable
#################################################

class Dog():
    def __init__(self,breed,name,spots):
        self.breed = breed
        self.name = name
        self.spots = spots



# creating an object and setting values in the object 
# my_dog = Dog(breed="Breed1" , name="Tommy", spots=False)
my_dog = Dog("Breed1" ,"Tommy", False)
print(type(my_dog))


# retrieving the values

ans  = my_dog.breed
print(ans)
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)









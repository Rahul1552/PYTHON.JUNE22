#################################################
#  18.08.2022 
#################################################
# TOPICS TO BE COVERED  
# OOP OBJECT ORIENTED PROGRAMMING
#################################################


#################################################
# attributes of class object
#################################################

print("******************************")


class Dog():
    species  = "mammal"

    def __init__(self,breed,name,spots):
        self.breed = breed
        self.name = name
        self.spots = spots

my_dog = Dog("Nagpur", "Tommy ", False)

print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
print(my_dog.species)


#################################################
# Methods
#################################################


print("***********Methods*******************")



class Dog():
    species  = "mammal"

    def __init__(self,breed,name,spots):
        self.breed = breed
        self.name = name
        self.spots = spots

    def bark(self,number):
        print("Woof Woof")
        print("The name of the dog is : {} and it will bark {} times ".format(self.name,number))

my_dog = Dog("Nagpur", "Tommy ", False)
my_dog.breed
my_dog.bark(15)



#################################################
# Some more Exxamples of class
#################################################


class Circle():
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    # def get_circumference(self):
    #     return 2*self.pi*self.radius

    # recommended way 

    def get_circumference(self):
        return 2*Circle.pi*self.radius

    def get_area(self):
        return Circle.pi*self.radius*self.radius


my_circle = Circle(15)
ans  = my_circle.get_circumference()
print(ans)

area_ans  = my_circle.get_area()
print(area_ans)


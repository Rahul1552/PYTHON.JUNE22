#################################################
#  19.08.2022 
#################################################
# TOPICS TO BE COVERED  
# INHERITANCE AND POLYMORPHISM
#################################################
class Animal():
    def __init__(self):
        print(("Animal is created"))
    
    def who_am_i(self):
        print("i Am an Animal")
    
    def eat(self):
        print("I am Eating")


my_animal = Animal()
my_animal.who_am_i()
my_animal.eat()

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Animal Dog is created ")

    # overwritng old method if required 
    def who_am_i(self):
        print("i Am A Dog")

    # adding new methods

    def bark(self):
        print("Woof Woof")

    

mydog = Dog()

mydog.who_am_i()
mydog.bark()



#################################################
# POLYMORPHISM
#################################################
print("***********POLYMORPHISM*******************")

class Dog():
    def __init__(self,name):
        self.name = name
    def speak(self):
        print(self.name + " says Woof Woof")

class Cat():
    def __init__(self,name):
        self.name = name
    def speak(self):
        print(self.name + " says meow")

class Frog():
    def __init__(self,name):
        self.name = name
    def speak(self):
        print(self.name + " says Croak")     

Tommy = Dog("Tommy")
Silly  = Cat("Silly")
Lewis = Frog("Lewis")



Tommy.speak()
Silly.speak()
Lewis.speak()
    


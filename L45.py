#################################################
#  20.08.2022 
#################################################
# TOPICS TO BE COVERED  
# SPECIAL/MAGIC METHODS
# https://docs.python.org/3/reference/datamodel.html#special-method-names
#################################################


#################################################
# SPECIAL/MAGIC METHODS
#################################################
class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author} "

    def __len__(self):
        return self.pages



b = Book("Learn Python Code ", "Rahul" , 250)
c = Book("Learn Python Code ", "Chinmay Sir" , 100)

print(b)
print(len(b))
print(len(c))

list1 = [1,3,6]
print(len(list1))


#################################################
# PASSBOOK MANAGEMENT
#################################################
# Account class
# deposit
# withdrawal


class Account:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,dep_amount):
        self.balance = self.balance + dep_amount
        print("Amount :  Rs. {} added to your acc".format(dep_amount))

    def withdrawal(self, wd_amount):
        self.wd_amount = wd_amount
        if self.balance > wd_amount:
            self.balance = self.balance - self.wd_amount
            print("Withdrawal done")
        else:
            print("You have insufficient balance")
    def __str__(self):
        return f"Balance :  {self.balance}"



a = Account("Rahul" ,2000)
a.deposit(1000)
a.deposit(1000)
print(a)

a.withdrawal(3000)

print(a)
#################################################
#  13.07.2022
#################################################
# TOPICS TO BE COVERED  
# 👉 TUPLES
# 👉 INSTALLING PYTHON AND VS-CODE
#################################################


capital_states= ("Bhopal","Mumbai","Imphal","Shillong","Aizawl","Kohima")

print(type(capital_states))

print(capital_states[3])
print(capital_states[2])
print(capital_states[0])
print(capital_states[-1])


# capital_states[0] = "Hyderabad" # will give you error 
# capital_states[1] = "Hyderabad" # will give you error

print(capital_states)
winter_capital = ("Nagpur",)
print(type(winter_capital))

capital = capital_states + winter_capital
print(capital)

# hOW TO EDIT TUPLE , IF NECESSARY 
y = list(capital_states) # type casting 
print(type(y))

x = tuple(y)
print(x)
print(type(x))

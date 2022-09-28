#################################################
#  26.08.2022 
#################################################
# TOPICS TO BE COVERED  
# RANDOM MODULES IN PYTHON
# https://docs.python.org/3/library/random.html#module-random
#################################################
import random

# from 0 to 1 , need to generate some random numbers(int/floats)
# ans  = random.random()
# print(ans)

#  for integer values
# limits are included in the result

# ans  = random.randint(1,10)
# print(ans)


# selecting from a list 

# lucky_num = [10,25,24,2,88,79]
# ans = random.choice(lucky_num)
# print(ans)

# vit_c = ["lemon", "orange" ,"fruit_c"]
# ans = random.choice(vit_c)
# print(ans)

# to select multiple random values from the given list
# ans = random.choices(vit_c , k=2)
# print(ans)

#################################################
#  TOSSING A COIN
#################################################

# import random

# list_ans = []
# for i in range(1,11):
#     list_coin = ["h" ,"t"]
#     ans  = random.choice(list_coin)
#     list_ans.append(ans)

# # print(list_ans)
# heads  = list_ans.count("h")
# print("Heads count is : " ,heads)
# tails  = list_ans.count("t")
# print("Tails count is : " ,tails)


#################################################
#  USER DEFINED MODULE
#################################################

import L51

L51.minus()
print(L51.sum1(10,30))
print(L51.__name__)
print(__name__)

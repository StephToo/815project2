# 815project2

My plan is to expand on my project 1's code that uses categroical distribution for my random samples with set probabilty.
I will chnage the code in order to add complexity, which is in that the probabilites are not set but rather are based on their
own probability distribution

In project 1 I model categorical distribution of voting. The probability is directly set, so I will change this aspect to a different
type of distribution. 

Here is code from proj 1: 
On lines 19 and 20 are what I will convert into probability distribution. I am considering using categorical prob dist
but am unsure of what is best. I will look into what kinds of distributions are used in modeling real elections and take inspiration from there. 

import numpy as np
import sys
import random as random

categories = ["Democrat", "Republican", "Other"]
probabilities1 = [0.3,0.5,0.2]
probabilities2 = [0.2,0.3,0.5]

values1 = np.cumsum(probabilities1)
values2 = np.cumsum(probabilities2)

np.random.rand()

#dataset1 = random.choices(categories, weights=probabilities1, k=100)
#dataset2 = random.choices(categories, weights=probabilities2, k=100)

dataset1 = np.random.rand(100)
dataset2 = np.random.rand(100)


condlist1 = [dataset1 <= limit for limit in values1]
condlist2 = [dataset2 <= limit for limit in values2]


sorted_data = sorted(dataset1 + dataset2)

with open('output.txt', 'w') as file:

 

# Close the file
file.close()

#file = open('numbers.txt', 'a')
#sys.stdout = file

#print(values1, file=open('numbers.txt', 'a'))
#print(values2, file=open('numbers.txt', 'a'))

#file.close()






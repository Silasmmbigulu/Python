#random number generation in python

import random

low = 1
high = 100

'''
number = random.randint(low, high)
print(number)
'''

'''
options = ("python","java", "html", "small_talk", "javascript", "sql")
option = random.choice(options)
print(option)
'''
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "k", "q", "a"]
random.shuffle(cards)
print(cards)



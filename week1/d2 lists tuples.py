

from os import popen
from numpy import append


mutable = can be can be changed
immutable = cannot be changed
# mutable (lists) vs immutable (tuples)
even_nums = [2, 4, 6, 8, 10] # mutable
odd_nums = (1, 3, 5, 7, 9) # immutable

even_nums[-1] = "ten"

odd_nums[-1] = "nine"

for i in even_nums:
    print(i)

array_example = [1, 2, 6, 7, 8, 4]
moving_median_3 = [2, 6, 7, ]

# Everything in Python is an object.

# #methods are e.g.
# append
# .pop



import numpy

print(dir(numpy))
print(numpy.sqrt(25))

from numpy import sqrt

print(sqrt(25))
# help(sqrt)

import random

print(random.choice(['a', 'b', 'c']))
print(random.choice(range(101)))
a = random.sample(range(101), 10)
print(a)

import statistics

print(statistics.mean(a))
print(statistics.median(a))

import os

print(os.getcwd())

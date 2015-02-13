import random
from search import *

# Binary Search

array = [random.randint(0, 100) for n in range(40)]
print('Binary Search:\n')
quick_sort(array)
print('List:\n', array)
key = random.randint(0, 100)
print('Key:\n', key, '\nFound:\n', binary_search(array, key))
print('\n')

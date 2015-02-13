import random
from sort_and_search import *

# Bubble Sort

array = [random.randint(0, 100) for n in range(40)]
print('Bubble Sort:\n')
print('Before:\n', array)
bubble_sort(array)
print('After:\n', array)
print('\n')

# Selection Sort

array = [random.randint(0, 100) for n in range(40)]
print('Selection Sort:\n')
print('Before:\n', array)
selection_sort(array)
print('After:\n', array)
print('\n')

# Insertion Sort

array = [random.randint(0, 100) for n in range(40)]
print('Insertion Sort:\n')
print('Before:\n', array)
insertion_sort(array)
print('After:\n', array)
print('\n')

# Shell Sort

array = [random.randint(0, 100) for n in range(40)]
print('Shell Sort:\n')
print('Before:\n', array)
shell_sort(array)
print('After:\n', array)
print('\n')

# Merge Sort

array = [random.randint(0, 100) for n in range(40)]
print('Merge Sort:\n')
print('Before:\n', array)
merge_sort(array)
print('After:\n', array)
print('\n')

# Quick Sort

array = [random.randint(0, 100) for n in range(40)]
print('Quick Sort:\n')
print('Before:\n', array)
quick_sort(array)
print('After:\n', array)
print('\n')

# Heap Sort

array = [random.randint(0, 100) for n in range(40)]
print('Heap Sort:\n')
print('Before:\n', array)
heap_sort(array)
print('After:\n', array)
print('\n')

# Binary Search

array = [random.randint(0, 100) for n in range(40)]
print('Binary Search:\n')
quick_sort(array)
print('List:\n', array)
key = random.randint(0, 100)
print('Key:\n', key, '\nFound:\n', binary_search(array, key))
print('\n')

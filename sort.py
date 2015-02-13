# Bubble Sort

def bubble_sort(array):
    sort = True
    last = len(array)
    for i in range(len(array)):
        for j in range(1, last):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
                sort = False
                last = j
        if sort:
            break

# Selection Sort

def selection_sort(array):
    
    for i in range(len(array)):
        min = i
        for j in range(i+1, len(array)):
            if array[min] > array[j]:
                min = j
        array[i], array[min] = array[min], array[i]

# Insertion Sort

def insertion_sort(array):
    
    for i in range(1, len(array)):
        j = i
        while j >= 1 and array[j-1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]
            j -= 1

# Shell Sort

def shell_sort(array):
    
    gap = 1
    while gap < len(array) // 3:
        gap = gap * 3 + 1
    
    while gap >= 1:
        for i in range(gap, len(array)):
            j = i
            while j >= 1 and array[j-gap] > array[j]:
                array[j-gap], array[j] = array[j], array[j-gap]
                j -= gap
        gap //= 3

# Merge Sort (top-down)

def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[0:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)
        
        l, r, k = 0, 0, 0

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                array[k] = left[l]
                l += 1
            else:
                array[k] = right[r]
                r += 1
            k += 1
        while l < len(left):
            array[k] = left[l]
            l += 1
            k += 1
        while r < len(right):
            array[k] = right[r]
            r += 1
            k += 1

# Quick Sort

def quick_sort(array):
    if len(array) > 1:
        key = len(array) // 2
        left = []
        right = []
        
        for i in range(len(array)):
            if i != key and array[i] <= array[key]:
                left.append(array[i])
            elif i != key and array[i] > array[key] :
                right.append(array[i])
        quick_sort(left)
        quick_sort(right)
        array[:] = left + [array[key]] + right

# Heap Sort

import heapq

def heap_sort(array):
    heapq.heapify(array)
    array[:] = [heapq.heappop(array) for i in range(len(array))]

# Radix Sort

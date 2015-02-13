# Binary Search

def binary_search(array, key):
    first = 0
    last = len(array) - 1

    while first <= last:
        mid = (first + last) // 2
        if array[mid] == key:
            return True
        else:
            if array[mid] < key:
                first = mid + 1
            else:
                last = mid - 1
    return False

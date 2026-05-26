from random import choice

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = choice(arr)
    left = [i for i in arr if i < pivot]
    middle = [i for i in arr if i == pivot]
    right = [i for i in arr if i > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

array = [5, 3, 9, 4, 4, 6, 10, 7]
print(quick_sort(array))
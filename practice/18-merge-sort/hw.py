from random import choice, randint
from time import perf_counter

def merge(left, right):
    sorted_list = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])        
    return sorted_list

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = choice(arr)
    left = [i for i in arr if i < pivot]
    middle = [i for i in arr if i == pivot]
    right = [i for i in arr if i > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

def measure(arr):
    start_m = perf_counter()
    merge_sort(arr)
    end_m = perf_counter()
    start_q = perf_counter()
    quick_sort(arr)
    end_q = perf_counter()
    t_m = end_m - start_m
    t_q = end_q - start_q
    print(f"merge_sort: {t_m}; quick_sort: {t_q}")
    diff = round(t_m / t_q * 100, 2)
    print(f"Diff: {diff}%")
    return diff

def run_attempts(arr, max_attempts=3):
    diff = measure(arr)
    for attempt in range(2, max_attempts + 1):
        if diff >= 100:
            break
        print(f"-- Attempt {attempt} --")
        diff = measure(arr)

max_n = 10
for n in range(1, 11):
    print(f"======== Test #{n} ========")
    print(f"interval: [-{max_n}; {max_n}]")
    arr = [randint(-max_n, max_n) for _ in range(1_000_000)]
    run_attempts(arr)
    print()
    max_n *= 10
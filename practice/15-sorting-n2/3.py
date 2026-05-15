def insertion_sort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j], arr[j + 1] = arr[j+1], arr[j]
            j -= 1
        arr[j + 1] = key

arr = [3, 9, 7, 5, 6, 11, 1]
insertion_sort(arr)
print(*arr)
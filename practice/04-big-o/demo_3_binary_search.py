import math


def linear_search(nums, target):
    steps = 0
    for num in nums:
        steps += 1
        if num == target:
            return steps
    return steps


def binary_search(nums, target):
    steps = 0
    left = 0
    right = len(nums) - 1
    while left <= right:
        steps += 1
        mid = (left + right) // 2
        if nums[mid] == target:
            return steps
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return steps



nums = list(range(1, 17))
target = 13

steps_l = linear_search(nums, target)
steps_b = binary_search(nums, target)

print(f"Массив: {nums}")
print(f"Ищем: {target}")
print()
print(f"Линейный поиск: {steps_l} шагов")
print(f"Бинарный поиск: {steps_b} шага")


print()
print(f"{'n':<16} {'Линейный':<16} {'Бинарный':<16}")
print("-" * 48)

for n in [10, 100, 1000, 1_000_000]:
    arr = list(range(n))
    target_last = n - 1
    steps_l = linear_search(arr, target_last)
    steps_b = binary_search(arr, target_last)
    print(f"{n:<16} {steps_l:<16} {steps_b:<16}")


print()
print("Теория для больших n:")
for n in [1_000_000_000, 10**18]:
    steps_b = math.ceil(math.log2(n + 1))
    print(f"  n = {n:>20_}  ->  бинарный: всего {steps_b} шагов")

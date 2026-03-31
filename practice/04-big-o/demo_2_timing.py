import time


def two_sum_cycle(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum_dict(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []


sizes = [100, 500, 1000, 2000, 5000, 10000]

print(f"{'n':<8} {'cycle (сек)':<16} {'dict (сек)':<16} {'%':<8}")
print("-" * (8 + 16 + 16 + 8 + 3))

for n in sizes:
    nums = list(range(n))
    target = n * 10

    start = time.perf_counter()
    two_sum_cycle(nums, target)
    time_cycle = time.perf_counter() - start

    start = time.perf_counter()
    two_sum_dict(nums, target)
    time_dict = time.perf_counter() - start

    print(f"{n:<8} {time_cycle:<16.4f} {time_dict:<16.6f} {time_cycle / time_dict * 100:7.0f}%")

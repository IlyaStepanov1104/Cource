# Two Sum — два решения


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


nums = [2, 7, 11, 15]
target = 9

print(f"two_sum_cycle: {two_sum_cycle(nums, target)}")    # [0, 1]
print(f"two_sum_dict: {two_sum_dict(nums, target)}")  # [0, 1]

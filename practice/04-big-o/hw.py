def ss(nums, target):
    s = {}
    for i in range(len(nums)):
        d = target - nums[i]
        if d in s:
            return [s[d], i]
        s[nums[i]] = i
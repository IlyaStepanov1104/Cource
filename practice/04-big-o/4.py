def bin_search(nums, target):
        left = 0
        right = len(nums) - 1 # 1 - 1 = 0

        while left <= right:
            middle = (right + left) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        return -1
    
    
print(bin_search([5], 5))
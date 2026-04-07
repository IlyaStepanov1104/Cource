class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        return len(s) != len(nums)
    
solution = Solution()
print(solution.containsDuplicate([1,2,3,1]))
print(solution.containsDuplicate([1,2,3]))
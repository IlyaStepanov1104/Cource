from typing import List


class Solution:
    def reverseString(self, s: List[str], start=0, end=None) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if end is None:
            end = len(s) - 1
            
        if start >= end:
            return
        
        s[start], s[end] = s[end], s[start]
        self.reverseString(s, start+1, end-1)
        
solution = Solution()
a = ['h', 'e', 'l', 'l', 'o']
solution.reverseString(a)
print(a)
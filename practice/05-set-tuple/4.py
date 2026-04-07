def numSquareSum(n: int) -> int:
    result = 0
    
    while n != 0:    
        i = n % 10
        n = n // 10
        result += i**2
    
    return result
    
class Solution: 
    def isHappy(self, n: int) -> bool:
        prev_n = set()
        while n != 1:
            prev_n.add(n)
            
            n = numSquareSum(n)

            if n in prev_n:
                return False
        
        return True   
        
        
solve = Solution()
print(f'returned - {solve.isHappy(2)}')
        
        
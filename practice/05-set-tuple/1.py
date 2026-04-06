class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapper = {}
        t_chars = set()
        for sc, tc in zip(s, t):
            if sc in mapper:
                if mapper[sc] != tc:
                    return False
            elif tc in t_chars:
                return False
            mapper[sc] = tc
            t_chars.add(tc)
        return True
    
    
print(Solution().isIsomorphic("egg", "add"))
print(Solution().isIsomorphic("f11", "b23"))
print(Solution().isIsomorphic("paper", "title"))
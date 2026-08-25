# O(n^2)
def first_unique_1(s):
    for i in range(len(s)):
        counter = 1
        for j in range(len(s)):
            if i != j and s[i] == s[j]:
                counter += 1
                break
            
        if counter == 1:
            return i
    
    return -1
        
# O(n)
def first_unique_2(s):
    freq = {}
    
    for i in s:
        freq[i] = freq.get(i, 0) + 1
        
    for i, char in enumerate(s):
        if freq[char] == 1:
            return i
        
    return -1
        
print(first_unique_2('leetcode'))
print(first_unique_2('loveleet'))
print(first_unique_2('aabb'))
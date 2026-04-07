def unique_chars(s):
    result_string = s.lower().replace(' ', '')
    
    return set(result_string)

print(unique_chars("hello world"))  # 7 (h,e,l,o,w,r,d)
print(unique_chars("Mississippi"))  # 4 (m,i,s,p)
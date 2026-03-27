bs = []
s = input().lower()
for i in range(len(s)):
    if s[i].isalpha()==True:
        bs.append(s[i])
k = ''.join(bs)
if k == k[::-1]: print('True')
else: print('False')






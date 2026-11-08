# LC 680: Valid Palindrome II
# https://leetcode.com/problems/valid-palindrome-ii/
# Дополнительно. Строчные латинские буквы. Можно удалить не более одного символа. Вернуть, можно ли получить палиндром. O(n) времени, O(1) дополнительной памяти, без срезов.

def valid_palindrome_ii(s: str) -> bool:
    pass




print(valid_palindrome_ii("abca"), True)
print(valid_palindrome_ii("abc"), False)
print(valid_palindrome_ii("aba"), True)
print(valid_palindrome_ii("a"), True)
print(valid_palindrome_ii("deeee"), True)
print(valid_palindrome_ii("eeeed"), True)

from Stack import Stack

# Задача: приходит строка из скобок. Определить - правильная ли скобочная последовательность?

def is_valid(s: str)-> bool:
    stack = Stack()
    for i in s:
        if i in ['(', '[', '{']:
            stack.push(i)
        else:
            if stack.is_empty():
                return False
            else:
                open = stack.pop()
                if i == ')' and open != '(' or i == ']' and open != '[' or  i == '}' and open != '{':
                    return False

    return stack.is_empty()


# --- True (правильные) ---
print(is_valid("()"))           # True
print(is_valid("(())"))         # True
print(is_valid("()()"))         # True
print(is_valid("[]"))           # True
print(is_valid("{}"))           # True
print(is_valid("()[]{}"))       # True
print(is_valid("({[]})"))       # True
print(is_valid("{[()]}"))       # True
print(is_valid("([{}])"))       # True
print(is_valid(""))             # True  (пустая строка - валидна)

# --- False (неправильные) ---
print(is_valid("("))            # False - не закрыта
print(is_valid(")"))            # False - нечем закрывать
print(is_valid(")("))           # False - не тот порядок
print(is_valid("(]"))           # False - не тот тип
print(is_valid("({)}"))         # False - перекрещиваются
print(is_valid("{[}]"))         # False - перекрещиваются
print(is_valid("((())"))        # False - лишняя открытая
print(is_valid("(()))"))        # False - лишняя закрытая

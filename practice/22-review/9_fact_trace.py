# Задача: Стек вызовов рекурсии
# Допиши print-трассировку fact(n), чтобы увидеть вход и выход каждого
# вызова, и сравни с тем, что ты расписал на бумаге для fact(4).


def fact(n, depth=0):
    print("  " * depth + f"-> fact({n})")
    if n <= 1:
        result = 1
    else:
        # TODO: рекурсивный вызов fact(n - 1, depth + 1), результат * n
        result = None
    print("  " * depth + f"<- fact({n}) = {result}")
    return result


print(fact(4))  # 24

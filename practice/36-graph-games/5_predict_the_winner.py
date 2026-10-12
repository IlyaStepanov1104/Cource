# LeetCode 486. Predict the Winner.
# Двое по очереди берут число с левого или правого края массива nums.
# Вернуть перевес первого игрока: на сколько его сумма больше суммы второго при идеальной игре обоих
# (если меньше - число отрицательное). Ответ задачи на LeetCode: перевес >= 0.
def advantage(nums: list[int]) -> int:
    n = len(nums)
    # best[l][r] - Лучший результат на массиве от nums[l] до nums[r] - [nums[l], nums[l+1], ..., nums[r-1], nums[r]]
    best = [[0] * n for _ in range(n)] 
    for i in range(n):
        # от nums[i] до nums[i] - [nums[i]]
        best[i][i] = nums[i]
    for length in range(2, n + 1):
        for l in range(n - length + 1):
            r = l + length - 1
            best[l][r] = max(
                nums[l] - best[l+1][r],
                nums[r] - best[l][r-1]
            )
    return best[0][n-1]


print(advantage([233]), 233)
print(advantage([1, 5]), 4)
print(advantage([1, 5, 2]), -2)
print(advantage([1, 5, 233, 7]), 222)
print(advantage([3, 9, 1, 2]), 7)
print(advantage([1, 1, 1, 1]), 0)

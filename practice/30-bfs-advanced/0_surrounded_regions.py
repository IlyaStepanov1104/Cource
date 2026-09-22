from collections import deque


# 130. Surrounded Regions
# Доска из 'X' и 'O'. Все области из 'O', полностью окружённые 'X',
# закрасить в 'X'. Область выживает, только если касается края доски.
# Доску менять на месте, ничего не возвращать.


def solve(board: list[list[str]]) -> None:
    pass




board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"],
]
solve(board)
print(board, [
    ["X", "X", "X", "X"],
    ["X", "X", "X", "X"],
    ["X", "X", "X", "X"],
    ["X", "O", "X", "X"],
])

board = [["X"]]
solve(board)
print(board, [["X"]])

board = [["O", "O"], ["O", "O"]]
solve(board)
print(board, [["O", "O"], ["O", "O"]])

board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "O"],
    ["X", "X", "X", "X"],
]
solve(board)
print(board, [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "O"],
    ["X", "X", "X", "X"],
])

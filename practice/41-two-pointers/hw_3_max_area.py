# LC 11: Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
# По желанию. Неотрицательные высоты стенок: найти максимум (r-l)*min(height[l],height[r]) для l<r. Не сортировать. O(n) времени и O(1) памяти.

def max_area(height: list[int]) -> int:
    pass




print(max_area([2, 1, 4, 3]), 6)
print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
print(max_area([1, 1]), 1)
print(max_area([0, 0, 0]), 0)

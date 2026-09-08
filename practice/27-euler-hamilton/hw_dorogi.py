n = int(input())
counter = 0

for _ in range(n):
    edges = [int(i) for i in input().split()]
    counter += sum(edges)

print(counter // 2)

# matrix = [[int(i) for i in input().split()] for _ in range(int(input()))]
# print(*matrix, sep='\n')
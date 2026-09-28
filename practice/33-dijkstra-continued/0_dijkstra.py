class Heap:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)
        i = len(self.data) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self.data[parent] <= self.data[i]:
                break
            self.data[parent], self.data[i] = self.data[i], self.data[parent]
            i = parent

    def pop(self):
        if not self.data:
            return None
        
        top = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            i = 0
            n = len(self.data)
            while True:
                left, right = 2 * i + 1, 2 * i + 2
                smallest = i
                if left < n and self.data[left] < self.data[smallest]:
                    smallest = left
                if right < n and self.data[right] < self.data[smallest]:
                    smallest = right
                if smallest == i:
                    break

                self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
                i = smallest
        return top

    def __len__(self):
        return len(self.data)

    def __bool__(self):
        return bool(self.data)

# Алгоритм Дейкстры: кратчайшее расстояние от source до всех вершин
# графа с неотрицательными весами рёбер.
# graph - список смежности: graph[u] = [(v, w), ...]
# w <= 10**5

def dijkstra(graph: list[list[tuple[int, int]]], source: int, n: int) -> list[float]:
    dist = [float('inf')] * n
    dist[source] = 0
    visited = [False] * n #visited[i] - посещена ли вершина i
    heap = Heap()
    heap.push((0, source))

    while heap:
        d, v = heap.pop() # type: ignore
        if visited[v]:
            continue
        visited[v] = True
        for to, w in graph[v]:
            if d + w < dist[to]:
                dist[to] = d + w
                heap.push((dist[to], to))

    return dist


graph = [
    [(1, 4), (2, 2)],
    [(3, 6)],
    [(3, 9), (1, 1)],
    [],
]
print(dijkstra(graph, 0, 4), [0, 3, 2, 9])

graph2 = [
    [(1, 1), (2, 5)],
    [(2, 1)],
    [],
]
print(dijkstra(graph2, 0, 3), [0, 1, 2])

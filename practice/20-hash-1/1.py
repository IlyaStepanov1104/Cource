def _hash(key, size) -> int:
    return sum([ord(s) % size for s in key]) % size

class HashTable:
    def __init__(self, size=10):
        self._size = size
        self._arr = [[] for i in range(size)]
        
    def set(self, key, value):
        index = _hash(key, self._size)
        for i in range(len(self._arr[index])):
            [k, _] = self._arr[index][i]
            if k == key:
                self._arr[index][i][1] = value
                return
        self._arr[index].append([key, value])
        
    def get(self, found_key):
        index = _hash(found_key, self._size)
        for [key, value] in self._arr[index]:
            if key == found_key:
                return value
        
    def has(self, found_key):
        index = _hash(found_key, self._size)
        for [key, _] in self._arr[index]:
            if key == found_key:
                return True

        return False


# --- примеры для отладки ---

# 1. Базовое наполнение — разные ключи в разные бакеты
t1 = HashTable(size=10)
t1.set("name", "Alice")
t1.set("name", "Bob")
t1.set("age", "30")
t1.set("city", "Moscow")
t1.set("job", "dev")
t1.set("lang", "Python")
print(t1.get('name'))

# 2. Коллизии — несколько ключей в одном бакете
# "ab" и "ba" дают одинаковый хэш (ord('a')+ord('b') == ord('b')+ord('a'))
t2 = HashTable(size=10)
t2.set("ab", 1)
t2.set("ba", 2)
t2.set("aab", 3)
t2.set("baa", 4)

# 3. get / has после коллизий
print(t2.get("ab"))   # 1
print(t2.get("ba"))   # 2
print(t2.has("aab"))  # True
print(t2.has("xyz"))  # False

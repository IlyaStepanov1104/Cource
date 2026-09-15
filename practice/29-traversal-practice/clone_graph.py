from collections import deque
from typing import Optional

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        copies = {node: Node(node.val)}
        q = deque([node])
        
        while q:
            v = q.popleft()
            for to in v.neighbors:
                if to not in copies:
                    copies[to] = Node(to.val)
                    q.append(to)
                copies[v].neighbors.append(copies[to])
                
        return copies[node]
    
                    
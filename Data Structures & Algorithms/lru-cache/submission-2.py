class Node:
    def __init__(self, key, value):
        self.val = value
        self.key = key
        self.prev = None 
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.next = Node(0, 0)
        self.prev = Node(0, 0)
        self.cache = {}
        self.prev.next = self.next
        self.next.prev = self.prev
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    def add(self, node):
        prev, nxt = self.next.prev, self.next
        prev.next = node
        nxt.prev= node 
        node.prev = prev
        node.next = nxt
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        return -1 
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.add(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.prev.next
            self.remove(lru)
            del self.cache[lru.key]
        


        

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.next = Node(0, 0)
        self.prev = Node(0, 0)
        self.next.prev = self.prev
        self.prev.next = self.next
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def add(self, node):
        prev, nxt = self.next.prev, self.next
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.add(self.cache[key])
        if self.capacity < len(self.cache):
            lru = self.prev.next
            self.remove(lru)
            del self.cache[lru.key]
        

        

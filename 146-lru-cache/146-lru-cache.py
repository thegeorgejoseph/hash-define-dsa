class Node:
    def __init__(self, key, value):
        self.key, self.val = key, value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.least, self.most = Node(0,0), Node(0,0)
        self.least.next, self.most.prev = self.most, self.least
        
    def remove(self, node):
        PREV, NEXT = node.prev, node.next
        PREV.next, NEXT.prev = NEXT, PREV
        
    def insert(self, node):
        prev = self.most.prev 
        prev.next = node
        node.prev = prev
        node.next = self.most
        self.most.prev = node
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            lru = self.least.next
            self.remove(lru)
            del self.cache[lru.key]
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
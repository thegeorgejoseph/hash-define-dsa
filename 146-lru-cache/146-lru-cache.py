class ListNode:
    def __init__(self, key, value):
        self.key, self.val = key, value
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.least, self.most = ListNode(0,0), ListNode(0,0)
        self.least.next, self.most.prev = self.most, self.least
    
    def remove(self, node):
        PREV, NEXT = node.prev, node.next
        PREV.next, NEXT.prev = NEXT, PREV
        
    def insert(self, node):
        mru = self.most.prev
        mru.next = node
        node.prev = mru
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
        
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            lru = self.least.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
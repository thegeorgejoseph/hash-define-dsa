class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next, self.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.least, self.most = ListNode(0,0), ListNode(0,0)
        self.least.next, self.most.prev = self.most, self.least

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val
    
    def remove(self, node):
        PREV, NXT = node.prev, node.next
        PREV.next, NXT.prev = NXT, PREV
    
    def insert(self, node):
        mru = self.most.prev
        mru.next = node
        node.prev = mru
        node.next = self.most
        self.most.prev = node
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.least.next
            self.remove(lru)
            del self.cache[lru.key]
            
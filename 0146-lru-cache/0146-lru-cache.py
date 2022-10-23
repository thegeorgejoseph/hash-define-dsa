class ListNode:
    def __init__(self, key = 0, val = 0, left = None, right = None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {} # key - > key, value
        self.cap = capacity
        self.least, self.most = ListNode(), ListNode()
        self.least.right, self.most.left = self.most, self.least

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val
    
    def remove(self, node):
        PRV, NXT = node.left, node.right
        PRV.right, NXT.left = NXT, PRV
    
    def insert(self, node):
        mru = self.most.left
        mru.right = node
        node.left = mru
        node.right = self.most
        self.most.left = node
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.least.right
            self.remove(lru)
            del self.cache[lru.key]
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
class ListNode:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left, self.right = None, None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.least, self.most = ListNode(0,0), ListNode(0,0)
        self.least.right, self.most.left = self.most, self.least
        
    def insert(self, node):
        mru = self.most.left
        mru.right = node
        node.left = mru
        node.right = self.most
        self.most.left = node
    
    def remove(self, node):
        PREV, NXT = node.left, node.right
        PREV.right, NXT.left = NXT, PREV

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
        else:
            return -1
        
        self.insert(self.cache[key])
        return self.cache[key].val

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
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {None:None}
        dummy = Node(0, head)
        current = head
        while current:
            hashmap[current] = Node(current.val)
            current = current.next
        current = head
        while current:
            node = hashmap[current]
            node.next = hashmap[current.next]
            node.random = hashmap[current.random]
            current = current.next
        return hashmap[dummy.next]
        
        
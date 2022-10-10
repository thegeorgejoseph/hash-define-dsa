# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cache = set([None])
        curr = headA
        while curr:
            cache.add(curr)
            curr = curr.next
        curr = headB
        while curr:
            if curr in cache:
                return curr
            curr = curr.next 

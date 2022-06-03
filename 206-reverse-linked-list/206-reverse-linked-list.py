# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        if current is None:
            return current
        prev = None
        while current is not None and current.next is not None:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        head = current
        head.next = prev
        return head
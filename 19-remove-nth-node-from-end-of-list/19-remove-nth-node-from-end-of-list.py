# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        current = dummy
        fast = head
        while n > 0:
            fast = fast.next
            n -= 1
        while fast:
            current = current.next
            fast = fast.next
        current.next = current.next.next
        return dummy.next
            
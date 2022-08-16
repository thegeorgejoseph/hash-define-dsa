# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        while n > 0:
            fast = fast.next
            n -= 1
        prev = dummy
        slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next
            prev = prev.next
        prev.next = slow.next
 
        return dummy.next 
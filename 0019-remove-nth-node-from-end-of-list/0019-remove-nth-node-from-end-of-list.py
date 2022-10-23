# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        k = 0
        curr = dummy
        while k < n:
            curr  = curr.next
            k += 1
        fast = curr
        slow = head
        prev = dummy
        while fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next
        prev.next = slow.next
        return dummy.next
        
        
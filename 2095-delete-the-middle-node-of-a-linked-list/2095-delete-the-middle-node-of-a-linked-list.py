# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow, fast = head, head
        prev = dummy
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        NXT = slow.next
        slow.next = None
        prev.next = NXT
        return dummy.next 
        
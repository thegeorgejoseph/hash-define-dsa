# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        curr = dummy
        h1, h2 = l1, l2
        while h1 or h2:
            if h1:
                carry += h1.val
                h1 = h1.next
            if h2:
                carry += h2.val
                h2 = h2.next
            tens, ones = divmod(carry, 10)
            carry = 0
            carry += tens
            curr.next = ListNode(ones)
            curr = curr.next
        if carry > 0:
            curr.next = ListNode(carry)
        
        return dummy.next

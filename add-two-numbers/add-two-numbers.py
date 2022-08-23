# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        h1, h2 = l1, l2
        curr = dummy
        while h1 or h2:
            if h1:
                carry += h1.val
                h1 = h1.next
            if h2:
                carry += h2.val
                h2 = h2.next
            if carry < 10:
                curr.next = ListNode(carry)
                carry = 0
            else:
                curr.next = ListNode(carry % 10)
                carry = carry // 10
            curr = curr.next
        if carry > 0:
            curr.next = ListNode(carry)
        
        return dummy.next
        

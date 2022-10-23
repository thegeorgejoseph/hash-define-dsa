# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        h1, h2 = l1, l2
        dummy = ListNode()
        curr = dummy
        while h1 or h2:
            if h1:
                carry += h1.val
                h1 = h1.next
            if h2:
                carry += h2.val
                h2 = h2.next
            
            div, mod = carry // 10, carry % 10
            carry = div
            curr.next = ListNode(mod)
            curr = curr.next
        if carry:
            curr.next = ListNode(carry)
        return dummy.next
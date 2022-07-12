# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        first, second = l1, l2
        dummy = ListNode()
        curr = dummy
        while first or second:
            res = carry
            if first:
                res += first.val
                first = first.next
            if second:
                res += second.val
                second = second.next
                
            if res < 10:
                carry = 0
            else:
                carry = res // 10
                res = res % 10
            
            curr.next = ListNode(res)
            curr = curr.next
        
        if carry > 0:
            curr.next = ListNode(carry)
        
        return dummy.next
        

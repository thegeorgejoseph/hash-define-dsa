# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        headOne, headTwo = l1, l2
        dummy = ListNode(0, None)
        current = dummy
        while headOne or headTwo:
            res = carry
            if headOne:
                res += headOne.val
                headOne = headOne.next
            if headTwo:
                res += headTwo.val
                headTwo = headTwo.next
                
            if res < 10:
                current.next = ListNode(res, None)
                carry = 0
            else:
                carry = res // 10
                current.next = ListNode(res % 10, None)
            
            current = current.next
        
        if carry > 0:
            current.next = ListNode(carry, None)
        
        return dummy.next
        
        
        
        
#         carry = 0
#         first, second = l1, l2
#         dummy = ListNode()
#         curr = dummy
#         while first or second:
#             res = carry
#             if first:
#                 res += first.val
#                 first = first.next
#             if second:
#                 res += second.val
#                 second = second.next
                
#             if res < 10:
#                 carry = 0
#             else:
#                 carry = res // 10
#                 res = res % 10
            
#             curr.next = ListNode(res)
#             curr = curr.next
        
#         if carry > 0:
#             curr.next = ListNode(carry)
        
#         return dummy.next
        

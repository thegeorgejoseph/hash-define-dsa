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
        
    
        # carry = 0
        # dummy = ListNode(0, None)
        # first, second = l1, l2
        # prev = dummy
        # while first or second:
        #     newVal = carry
        #     if first:
        #         newVal += first.val
        #         first = first.next
        #     if second:
        #         newVal += second.val
        #         second = second.next
        #     if newVal < 10:
        #         carry = 0
        #     else:
        #         carry = newVal // 10
        #         newVal = newVal % 10
        #     prev.next = ListNode(newVal, None)
        #     nextNode = prev.next
        #     prev = prev.next
        # if carry > 0:
        #     prev.next = ListNode(carry, None)
        # return dummy.next
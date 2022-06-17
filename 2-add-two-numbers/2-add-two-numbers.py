# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0, None)
        first, second = l1, l2
        prev = dummy
        while first or second:
            newVal = carry
            if first:
                newVal += first.val
                first = first.next
            if second:
                newVal += second.val
                second = second.next
            if newVal < 10:
                carry = 0
            else:
                carry = newVal // 10
                newVal = newVal % 10
            prev.next = ListNode(newVal, None)
            nextNode = prev.next
            prev = prev.next
        if carry > 0:
            prev.next = ListNode(carry, None)
        return dummy.next
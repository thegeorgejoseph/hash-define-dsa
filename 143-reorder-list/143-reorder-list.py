# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        current = slow.next
        slow.next = None
        
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        first, second = head, prev
        while first and second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            second = temp2
            first = temp1
            
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
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        h1, h2 = head, prev
        while h1 and h2:
            temp = h1.next 
            h1.next = h2
            h1 = temp
            temp = h2.next
            h2.next = h1
            h2 = temp
        
        
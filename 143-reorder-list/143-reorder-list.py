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
        
        curr = slow.next
        slow.next = None
        prev = None  
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        first, second = head, prev
        while first and second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        
            
#         slow, fast = head, head.next
#         while fast and fast.next: #we check for fast.next so that we can keep track of the centre accurately
#             slow = slow.next
#             fast = fast.next.next
        
        
#         current = slow.next
#         slow.next = None # this is to turn the first halfs last link off
#         prev = None
#         while current:
#             nextNode = current.next
#             current.next = prev
#             prev = current
#             current = nextNode
        
#         #prev will hold the second head now
#         #head will hold the original head
        
#         first, second = head, prev
#         while first and second:
#             temp1, temp2 = first.next, second.next
#             first.next = second
#             second.next = temp1
#             first = temp1
#             second = temp2
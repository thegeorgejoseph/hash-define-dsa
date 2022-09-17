# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        h1, h2 = list1, list2
        while h1 and h2:
            if h1.val <= h2.val:
                temp = h1.next
                curr.next = h1
                h1 = temp
            else:
                temp = h2.next
                curr.next = h2
                h2 = temp
            curr = curr.next
        if h1:
            curr.next = h1
        if h2:
            curr.next = h2
        
        return dummy.next
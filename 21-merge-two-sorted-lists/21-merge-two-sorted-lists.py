# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        headOne, headTwo = list1, list2
        current = dummy
        while headOne is not None and headTwo is not None:
            if headOne.val <= headTwo.val:
                temp = headOne.next
                current.next = headOne
                current = headOne
                headOne = temp
            else:
                temp = headTwo.next
                current.next = headTwo
                current = headTwo
                headTwo = temp
                
        if headOne is not None:
            current.next = headOne
        if headTwo is not None:
            current.next = headTwo
        return dummy.next
        
        
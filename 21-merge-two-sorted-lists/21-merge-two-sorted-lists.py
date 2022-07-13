# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        headOne, headTwo = list1, list2
        
        while headOne is not None and headTwo is not None:
            if headOne.val <= headTwo.val:
                temp1 = headOne.next
                current.next = headOne
                current = current.next
                headOne = temp1
            else:
                temp2 = headTwo.next
                current.next = headTwo
                current = current.next
                headTwo = temp2
        if headOne:
            current.next = headOne
        if headTwo:
            current.next = headTwo
        return dummy.next
        
        
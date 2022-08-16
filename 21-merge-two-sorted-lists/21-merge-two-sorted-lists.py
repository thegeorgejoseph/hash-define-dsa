# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        current = dummy
        headOne, headTwo = list1, list2
        while headOne and headTwo:
            if headOne.val <= headTwo.val:
                temp = headOne.next
                current.next = headOne
                current = current.next
                headOne = temp
            else:
                temp = headTwo.next
                current.next = headTwo
                current = current.next
                headTwo = temp
        if headOne:
            current.next = headOne
        if headTwo:
            current.next = headTwo
        return dummy.next
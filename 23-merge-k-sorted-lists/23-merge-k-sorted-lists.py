# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        headOne, headTwo = l1, l2
        while headOne and headTwo:
            if headOne.val <= headTwo.val:
                temp = headOne.next
                curr.next = headOne
                headOne = temp
            else:
                temp = headTwo.next
                curr.next = headTwo
                headTwo = temp
            curr = curr.next
        if headOne:
            curr.next = headOne
        if headTwo:
            curr.next = headTwo
        return dummy.next
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        res = []
        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                temp.append(self.mergeTwoLists(l1, l2))
            lists = temp[:]
        return lists[0]
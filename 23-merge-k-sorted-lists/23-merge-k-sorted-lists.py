# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeLists(self, list1,list2):
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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                temp.append(self.mergeLists(l1,l2))
            lists = temp
        
        return lists[0]
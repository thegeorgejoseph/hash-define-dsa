# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                temp.append(self.mergeTwoLists(l1,l2))
            lists = temp
        
        return lists[0]
    
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        current = dummy
        
        headOne, headTwo = l1, l2
        
        while headOne is not None and headTwo is not None:
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
                
            
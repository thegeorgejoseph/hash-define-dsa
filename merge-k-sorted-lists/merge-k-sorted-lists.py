# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        h1, h2 = l1, l2
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

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists),2):
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < len(lists) else None
                temp.append(self.mergeTwoLists(list1,list2))
            lists = temp[:]
        return lists[0]
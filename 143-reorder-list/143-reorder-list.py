# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        h2 = slow.next
        slow.next = None
        curr = h2
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        h1, h2 = head, prev
        dummy = ListNode(0, h1)
        while h1 and h2:
            h1_nxt = h1.next
            h1.next = h2
            h1 = h1_nxt
            h2_nxt = h2.next
            h2.next = h1
            h2 = h2_nxt
        return dummy.next
        
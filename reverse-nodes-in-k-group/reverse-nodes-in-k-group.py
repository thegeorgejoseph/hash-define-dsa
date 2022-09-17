# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getKthNode(self, curr, k):
        while curr and k > 0:
            k -= 1
            curr = curr.next
        return curr
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        currPrev = dummy
        
        while True:
            kthNode = self.getKthNode(currPrev, k)
            if not kthNode:
                break
            currNext = kthNode.next
            curr = currPrev.next
            prev = currNext
            while curr != currNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            temp = currPrev.next
            currPrev.next = kthNode
            currPrev = temp
        return dummy.next
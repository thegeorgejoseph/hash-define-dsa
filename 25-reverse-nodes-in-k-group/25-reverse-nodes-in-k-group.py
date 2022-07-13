# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        currentPrev = dummy
        
        while True:
            kth = self.getKthNode(currentPrev, k)
            
            if not kth:
                break
            
            currentNext = kth.next
            
            prev, curr = currentNext, currentPrev.next
            while curr != currentNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            tmp = currentPrev.next
            currentPrev.next = kth
            currentPrev = tmp
        
        return dummy.next
            
            
    def getKthNode(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1
        return node
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
We select the middle element as the node each time 
Use pointers rather than slices because otherwise the amount of memory taken will be O(N*N) 


'''
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(l,r):
            if l > r or r < l:
                return 
            mid  = l + ((r-l)//2)
            node = TreeNode(nums[mid])
            node.left = dfs(l, mid-1)
            node.right = dfs(mid + 1, r)
            return node
        return dfs(0, len(nums)-1)
        
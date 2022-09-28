# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        cache = defaultdict(list) # x-values: node.val
        queue = deque([(0,root)])
        while queue:
            x, node = queue.popleft()
            cache[x].append(node.val)
            if node.left:
                queue.append((x-1,node.left))
            if node.right:
                queue.append((x + 1, node.right))
        min_x = min(cache.keys())
        max_x = max(cache.keys())
        res = []
        for i in range(min_x, max_x + 1):
            if cache[i]:
                res.append(cache[i])
        return res
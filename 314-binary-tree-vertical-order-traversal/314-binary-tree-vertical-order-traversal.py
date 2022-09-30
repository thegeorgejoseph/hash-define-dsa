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
        cache = defaultdict(list)
        queue = deque([(0,root)])
        
        while queue:
            for i in range(len(queue)):
                x, top = queue.popleft()
                cache[x].append(top.val)
                if top.left:
                    queue.append((x - 1, top. left))
                if top.right:
                    queue.append((x + 1, top.right))
            
                
        min_x, max_x = min(cache.keys()), max(cache.keys())
        res = []
        for x in range(min_x, max_x + 1):
            if cache[x]: res.append(cache[x])
        return res
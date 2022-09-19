# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        res = []
        def dfs(node):
            if not node:
                res.append("NULL")
                return 
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            return 
        
        dfs(root)
        return ",".join(res)
        

    def deserialize(self, data):
        nodes = data.split(",")
        self.i = 0
        
        def dfs():
            if nodes[self.i] == "NULL":
                self.i += 1
                return 
            
            curr = TreeNode(nodes[self.i])
            self.i += 1
            left = dfs()
            right = dfs()
            curr.left = left
            curr.right = right
            return curr
        
        return dfs()
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
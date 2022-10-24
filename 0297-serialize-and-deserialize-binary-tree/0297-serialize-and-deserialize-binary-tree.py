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
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(map(str, res))

    def deserialize(self, data):
        nodes = data.split(",")
        self.i = 0
        
        def dfs():
            if nodes[self.i] == "NULL":
                self.i += 1
                return 
            
            root = TreeNode(int(nodes[self.i]))
            self.i += 1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
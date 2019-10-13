# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        res = []
        self.dfs(root,0,res)
        return res
    
    def dfs(self,root, level, res):
        if not root:
            return None
        if len(res) < level + 1:
            res.append([])
            
        res[level].append(root.val)
        self.dfs(root.left,level + 1,res)
        self.dfs(root.right, level + 1, res)

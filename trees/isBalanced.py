# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        if root is None:
            return True
            
        return abs(self.getHeight(root.left) - self.getHeight(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def getHeight(self,node):
        if node is None:
            return 0
        
        return 1 + max(self.getHeight(node.left), self.getHeight(node.right)) 

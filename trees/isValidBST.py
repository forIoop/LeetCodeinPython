# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValidBSTHelper(root,float("-inf"),float("inf"))
    
    def isValidBSTHelper(self,node,minValue,maxValue):
        
        if node is None:
            return True
        
        if node.val <= minValue or node.val >= maxValue:
            return False
        
        leftIsValid = self.isValidBSTHelper(node.left,minValue,node.val)
        rightIsValid = self.isValidBSTHelper(node.right,node.val,maxValue)
        
        return leftIsValid and rightIsValid
        

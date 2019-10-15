# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None 
    

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.findSegments(root);
        temp = firstStartPoint.val
        firstStartPoint.val = lastEndPoint.val
        lastEndPoint.val = temp
        return root
    
    def findSegments(self,root):
        firstStartPoint = None
        lastEndPoint = None
        prevNode = None
        
        if node == None:
            return None
        self.findSegments(node.left)
        if prevNode != None:
            if prevNode.val > node.val
                if firstStartPoint == None:
                    firstStartPoint = prevNode
                lastEndPoint = node
                
        prevNode = node
        self.findSegments(root.right)
                

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        
        if root == None:
            return True
        return self.checkMirror(root.left,root.right)
    
    def checkMirror(self,leftSubTree,rightSubTree):
        if leftSubTree == None and rightSubTree == None:
            return True
        elif leftSubTree != None and rightSubTree != None:
            return leftSubTree.val == rightSubTree.val and self.checkMirror(leftSubTree.left,rightSubTree.right) and self.checkMirror(leftSubTree.right, rightSubTree.left)
        return False

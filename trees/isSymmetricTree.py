# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        # Case where root is null, else check left and right values
        return root == None or self.check(root.left,root.right)
    
    #Checks if the left and right values of our left and right subtrees are equal
    def check(self,leftSub,rightSub):
        #returns true if the subtrees are none, Base case that evaluates to true if equal
        if leftSub == None and rightSub == None:
            return True
        #Case where Subtrees are not None, then compare the values
        elif leftSub != None and rightSub != None:
            #recursion that checks if the trees are symettrical
            return leftSub.val == rightSub.val and self.check(leftSub.left, rightSub.right) and self.check(leftSub.right, rightSub.left)
        
        return False    
                 
        """

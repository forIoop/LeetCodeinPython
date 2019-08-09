# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def range_sum_bst(root, L, R):
    result = 0
    
    #append to result if the values are in between
    if root.val >=L and root.val <= R:
        result += root.val
    
    #if a root.left exists, keep going left
    if root.left:
        result += range_sum_bst(root.left,L,R)
        

    #if a root.right exists, keep going right
    if root.right:
        result += range_sum_bst(root.right,L,R)
    
    return result
    
    
    

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
            return range_sum_bst(root, L, R)

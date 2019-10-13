 Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        info = []
        def DFS(node, depth = 0):
            if node is not None:
                if len(info) <= depth:
                    info.append([0,0])
                info[depth][0] += node.val
                info[depth][1] += 1
                DFS(node.left, depth + 1)
                DFS(node.right, depth + 1)
        DFS(root)
        return [value/float(numbers) for value, numbers in info]

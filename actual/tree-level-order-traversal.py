
class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        nodes = []
        nodeDeque = deque([root])

        while nodeDeque:
            levelLen = len(nodeDeque)
            levelNodes = []
            for i in range(levelLen):
                curNode = nodeDeque.popleft()
                levelNodes.append(curNode.val)
                if curNode.left:
                    nodeDeque.append(curNode.left)
                if curNode.right:
                    nodeDeque.append(curNode.right)
            nodes.append(levelNodes)

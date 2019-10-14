def levelOrderBottom(self, root):
        
        res = []
        self.dfs(root,0,res)
        return res[::-1]
    
    def dfs(self,node,level,res):
        
        if not node:
            return None
        if len(res) < level + 1:
            res.append([])
        res[level].append(node.val)
            
        self.dfs(node.left,level + 1,res)
        self.dfs(node.right,level + 1,res)
        

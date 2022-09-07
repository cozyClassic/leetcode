class Solution:
    result = ""
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            self.result += str(node.val)
            
            if node.left and node.right :
                self.result += "("
                dfs(node.left)
                self.result += ")("
                dfs(node.right)
                self.result+= ")"
                
            elif node.left and not node.right :
                self.result += "("
                dfs(node.left)
                self.result += ")"
                
            elif not node.left and node.right :
                self.result += "()("
                dfs(node.right)
                self.result += ")"
            
            return dfs
    
        dfs(root)
        
        return self.result
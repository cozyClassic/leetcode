class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        result = ""
        def dfs(node):
            nonlocal result
            result += "("
            result += str(node.val)
            
            if node.left :
                dfs(node.left)
                result+= ")"
                
                if node.right :
                    dfs(node.right)
                    result+= ")"
            
            elif node.right :
                result += "()"
                dfs(node.right)
                result += ")"
                
            else:
                return
    
        dfs(root)
        
        return result[1:]
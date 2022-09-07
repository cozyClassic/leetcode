class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        result = ""
        def dfs(node):
            if not node :
                return
            nonlocal result
            result += str(node.val)
            
            if not node.left and not node.right:
                return

            result += "("
            dfs(node.left)
            result += ")"
            if node.right :
                result += "("
                dfs(node.right)
                result+= ")"

        dfs(root)
        return result

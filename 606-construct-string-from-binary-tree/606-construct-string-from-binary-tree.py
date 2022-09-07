class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        result = []
        def dfs(node):
            if not node :
                return
            result.append(str(node.val))
            
            if not node.left and not node.right:
                return

            result.append("(")
            dfs(node.left)
            result.append(")")
            if node.right :
                result.append("(")
                dfs(node.right)
                result.append(")")
        dfs(root)
        return "".join(result)

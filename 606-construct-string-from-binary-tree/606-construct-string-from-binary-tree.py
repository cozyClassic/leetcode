class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        result = []
        def dfs(node):
            result.append(str(node.val))
            if node.left :
                result.append("(")
                dfs(node.left)
                result.append(")")
                if node.right :
                    result.append("(")
                    dfs(node.right)
                    result.append(")")
            elif node.right :
                result.append("()(")
                dfs(node.right)
                result.append(")")
        dfs(root)
        return "".join(result)
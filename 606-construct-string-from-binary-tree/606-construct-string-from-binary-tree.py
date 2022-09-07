class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        result = ""
        def dfs(node):
            nonlocal result
            result += str(node.val)
            if node.left :
                result += "("
                dfs(node.left)
                result+= ")"
                if node.right :
                    result += "("
                    dfs(node.right)
                    result+= ")"
            elif node.right :
                result += "()("
                dfs(node.right)
                result += ")"
        dfs(root)
        return result

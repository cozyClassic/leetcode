class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]

        def dfs(array, node):
            if node.left:
                dfs(array, node.left)
            if node.right:
                dfs(array, node.right)
            array.append(node.val)
        result = []
        dfs(result,root)
        return result
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        Q = []
        Q.append((root, root.val))

        while Q :
            node, _max = Q.pop()
            if node is None:
                continue
            if node.val >= _max:
                result += 1
                _max = node.val
            Q.append((node.left, _max))
            Q.append((node.right, _max))           

        return result
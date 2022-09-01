# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        Q = deque()
        Q.append((root, root.val))
        
        
        while Q :
            node, _max = Q.popleft()
            if node is None:
                continue
            if node.val >= _max:
                result += 1
                _max = node.val
            Q.append((node.left, _max))
            Q.append((node.right, _max))           

        return result
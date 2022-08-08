# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []
        Q =deque()
        Q.append((root, 0)) # level
        result_dict = defaultdict(list)
        
        while Q :
            node, level = Q.popleft()
            result_dict[level].append(node.val)
            
            if node.left :
                Q.append((node.left, level - 1))
            
            if node.right :
                Q.append((node.right, level + 1))
        
        levels = list(result_dict.keys())
        levels.sort()
        
        return [result_dict[level] for level in levels]
        
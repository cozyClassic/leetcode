# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        L = root.left
        R = root.right
        Q = deque()
        Q.append((L,R))
        
        while Q :
            left, right = Q.popleft()
            if left is None and right is None:
                continue
            if left == None or right == None:
                return False
            
            if left.val != right.val :
                return False
            
            Q.append((left.left, right.right))
            Q.append((left.right, right.left))
        
        return True
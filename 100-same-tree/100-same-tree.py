# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:        
        Q = deque()
        
        Q.append((p,q))
        
        while Q :
            p_n, q_n = Q.popleft()
            if (p_n == None and q_n != None) or (p_n != None and q_n == None):
                return False
            if p_n == None and q_n == None:
                continue
                
            if p_n.val != q_n.val :
                return False
            Q.append((p_n.left,q_n.left))
            Q.append((p_n.right,q_n.right))
        
        return True
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        Q = deque()
        Q.append((root.left,root.right))
        
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
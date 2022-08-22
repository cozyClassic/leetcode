# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    leafs = []
    def is_leaf(self, node:TreeNode):
        return node.left is None and node.right is None

    def DFS(self, node:TreeNode):
        if node.left and self.is_leaf(node.left):
            self.leafs[-1].append(node.left.val)
            node.left = None
        elif node.left :
            self.DFS(node.left)
        
        if node.right and self.is_leaf(node.right):
            self.leafs[-1].append(node.right.val)
            node.right = None
        elif node.right:
            self.DFS(node.right)

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.leafs = []
        while not self.is_leaf(root):
            self.leafs.append([])
            self.DFS(root)
        
        self.leafs.append([root.val])
        
        return self.leafs
    
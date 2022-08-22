class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        maxval = 0
        def longest_path(root: TreeNode) -> List[int]:
            nonlocal maxval
            r_l, r_r = root.left, root.right
            
            if not root:
                return [0, 0]
            
            inr = dcr = 1
            if r_l:
                left = longest_path(r_l)
                if (root.val == r_l.val + 1):
                    dcr = left[1] + 1
                elif (root.val == r_l.val - 1):
                    inr = left[0] + 1
            
            if r_r:
                right = longest_path(r_r)
                if (root.val == r_r.val + 1):
                    dcr = max(dcr, right[1] + 1)
                elif (root.val == r_r.val - 1):
                    inr = max(inr, right[0] + 1)
                    
            maxval = max(maxval, dcr + inr - 1)
            return [inr, dcr]
        
        longest_path(root)
        return maxval
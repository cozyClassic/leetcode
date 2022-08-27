class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        _sum = 0
        for n1, n2 in zip(self.nums, vec.nums):
            if 0 in (n1,n2):
                continue
            _sum += n1*n2
        
        return _sum

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
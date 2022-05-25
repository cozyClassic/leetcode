class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        results = [0]
        prev = 0
        for num in nums:
            curr = prev + num
            if curr > 0 :
                results.append(curr)
                prev = curr
            else:
                prev = 0
        
        return max(nums) if len(results) == 1 else max(results)
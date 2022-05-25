class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = []
        curr = 0
        prev = -1
        while curr < len(nums) - 1:
            max_reach = self.get_next_reach(nums[prev+1:curr+1])
            dp.append(max_reach)
            prev = curr
            curr += max_reach
            if curr == prev: return 0
        return len(dp)
        
        
        return results[-1]

    def get_next_reach(self, L):
        reach = 0
        for i, num in enumerate(L):
            reach = max(reach, num - (len(L)-i-1))
        return reach
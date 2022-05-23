class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        N = len(nums)
        results = [0] * (N-1)
        
        for i in range(N-1):
            results[i] = nums[i] + i
        
        goal = N-1
        count = 0
        curr = -1
        while results:
            curr = results.pop()
            count += 1
            if curr >= goal:               
                goal = N - count -1
              
        return curr >= goal
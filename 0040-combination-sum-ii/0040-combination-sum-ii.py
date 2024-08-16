from typing import List

class Solution:
    def dfs(self, nums, goal, curr):
        if not nums:
            return []
        for i, num in enumerate(nums):
            if num == nums[i-1]:
                continue
            if num == goal:
                self.result.add(tuple(curr[:]+[num]))
            elif num < goal:
                r = self.dfs(nums[i+1:], goal-num, curr[:]+[num])
                if r:
                    self.result += tuple(r)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()    
        self.result = set()
        self.dfs(candidates,target,[])

        return self.result

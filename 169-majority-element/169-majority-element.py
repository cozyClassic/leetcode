from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        goal = len(nums)//2
        
        for num in nums :
            counts[num] += 1
            
            if counts[num] > goal :
                return num
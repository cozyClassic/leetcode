class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1 :
            return nums[0]
    
        result_list=[{"pos":0,"neg":0} for _ in nums]
        for i, num in enumerate(nums) :
            if num > 0 :
                result_list[i]["pos"] = num
            elif num < 0:
                result_list[i]["neg"] = num

        for i, num in enumerate(nums):
            if i == 0 :
                continue
            prev,curr = result_list[i-1], result_list[i]
            pos, neg  = prev["pos"], prev["neg"]
            if num > 0:
                if pos != 0 :
                    curr["pos"] = pos * num
                if neg != 0 :
                    curr["neg"] = neg * num
            elif num < 0 :
                if pos != 0 :
                    curr["neg"] = pos * num
                if neg != 0 :
                    curr["pos"] = neg * num
    
        
        return max([r["pos"] for r in result_list])
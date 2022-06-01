import sys
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ar_list_lens = []
        count = 0
        gap = 2001
        prev = nums[0]
        
        for num in nums[1:] :
            if num - prev == gap :
                count += 1
            else :
                if count >= 2:
                    ar_list_lens.append(count+1)
                gap = num - prev
                count = 1
            prev = num
        
        if count >= 2:
            ar_list_lens.append(count+1)
         
        result = 0
        for length in ar_list_lens :
            result += (length-1) * (length-2) // 2
        
        return result
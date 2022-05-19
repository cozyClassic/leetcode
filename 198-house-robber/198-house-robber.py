class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2 :
            return max(nums)
    
        sums_dict = dict()
        prev = nums[0]
        sums_dict[0] = (True,prev)
        sums_dict[-1] = (False,0)
        
        for i, num in enumerate(nums) :
            # 이전 값이 포함되어 있을 때
            if sums_dict[i-1][0] :
                if sums_dict[i-2][1] + num > sums_dict[i-1][1] :
                    sums_dict[i] = (True, sums_dict[i-2][1] + num)
                else :
                    sums_dict[i] = (False, sums_dict[i-1][1])
                
            # 직전 값이 포함되어 있지 않을 때
            else :
                sums_dict[i] = (True, sums_dict[i-1][1] + num)
            
            perv = num
        
        L = len(nums) - 1
        return max(sums_dict[L][1], sums_dict[L-1][1])
        
        
# 각 인덱스에 대해서, (본인포함여부(True/False), 합계)를 밸류로 하는 딕셔너리를 만든다.
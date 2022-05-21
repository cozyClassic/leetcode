class Solution:
    def deleteAndEarn(self, nums) -> int:
        result = 0
        #1. change data to [(num, sum_of_num),(),..)
        sum_list = self.get_sum_list(nums)
        
        if len(sum_list) == 1 :
            return sum_list[0][1]
        
        if len(sum_list) == 2 :
            if (sum_list[0][0] + 1 == sum_list[1][0]):
                return max(sum_list[0][1], sum_list[1][1])
            return sum_list[0][1] + sum_list[1][1]
            
        
        #2. make result list for DP
        result_list = {num: (0, False) for num, _ in sum_list}
        result_list[-1] = (0,True)
        sum_list.insert(0,(-1,0))
        
        for i in range(1, len(sum_list)) :
            # 차이가 1만큼만 나는 경우
            curr_num = sum_list[i][0]
            prev_num = sum_list[i-1][0]
            pprev_num = sum_list[i-2][0]
            curr_sum = sum_list[i][1]
            if (curr_num - prev_num) == 1 and result_list[prev_num][1] :
                if (result_list[pprev_num][0] + curr_sum) > result_list[prev_num][0] :
                    result_list[curr_num] = (result_list[pprev_num][0] + curr_sum, True)
                else :
                    result_list[curr_num] = (result_list[prev_num][0], False)                
                continue

            result_list[curr_num] = ((result_list[prev_num][0] + curr_sum), True)
        
        return max([result_list[num][0] for num in result_list])
            
    def get_sum_list(self, nums):
        from collections import defaultdict
        num_count = defaultdict(int)
        for num in nums:
            num_count[num] += num
        
        sum_list = [(num,num_count[num]) for num in num_count]
        sum_list.sort()
        
        return sum_list
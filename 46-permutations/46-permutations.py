class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        L = len(nums)

        def dfs(num_list,append_list) :
            if len(num_list) == L:
                result.append(num_list)
                return

            for i in range(len(append_list)):
                dfs(num_list+[append_list[i]], append_list[:i]+append_list[i+1:])

        dfs([],nums)

        return result
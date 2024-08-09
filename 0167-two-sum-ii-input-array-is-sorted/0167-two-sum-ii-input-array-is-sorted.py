class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, v in enumerate(numbers):
            d = target - v
            if d in seen:
                return [seen[d]+1, i+1]
            seen[v] = i
            
        return [-1,-1]
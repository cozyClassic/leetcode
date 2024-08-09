"""
1. (중앙에서 가장 멀리있는) 2번째로 높은 높이를 찾는다.
2. 
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        result = 0

        while l < r:
            L = height[l]
            R = height[r]
            result = max(result, abs(min(L,R))*(r-l))
            if L <= R:
                l += 1
            else:
                r -= 1

        return result

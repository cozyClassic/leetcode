from typing import List
from collections import deque
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        result = 0

        while nums:
            curr_len = 0
            Q = deque()
            start = nums.pop()
            Q.append(start)
            nums.add(start)
            while Q:
                num = Q.popleft()
                if not num in nums:
                    continue
                nums.remove(num)
                curr_len += 1
                Q.append(num+1)
                Q.append(num-1)
            result = max(result, curr_len)

        return result
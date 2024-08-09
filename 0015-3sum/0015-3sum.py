class Solution:
    # nums2 is already sorted
    def twoSum(self, nums2, goal):
        result = set()
        seen = set()
        for n in nums2:
            remain = goal - n
            if remain in seen:
                result.add(tuple([-goal, n, remain]))
            seen.add(n)
        return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # i,j,k는 모두 달라야 함. 합은 0이어야 함
        nums.sort()
        result = set()
        for i in range(len(nums)-2):
            n1 = nums[i]
            combs = self.twoSum(nums[i+1:], -n1)
            result = result.union(combs)
        return list(result)

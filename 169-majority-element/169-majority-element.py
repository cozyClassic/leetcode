class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums :
            return None
        
        if len(nums) == 1 :
            return nums[0]
        
        H = len(nums)//2
        
        a = self.majorityElement(nums[:H])
        b = self.majorityElement(nums[H:])
        
        if nums.count(a) > H: 
            return a
        return b

"""분할정복 :
병합정렬과의 비교
- 병합정렬 : 쪼갠 다음 정렬해서 각각의 엘리먼트를 전부 반환
- 여기서는 ..? 과반수 후보군에 해당하는 요소만 반환.

a = function(nums[:len(nums)//2])
b = function(nums[len(nums)//2:])
이렇게 잘라주고 재귀함수를 돌리면, a,b는 모두 마지막에는
"최소 단위로 쪼개진 nums의 element"를 갖게된다.

"""
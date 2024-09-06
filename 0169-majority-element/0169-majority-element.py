class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def divide_conquer(nums,l,r) :
            if l == r:
                 return (nums[l], 1)
            mid = (l + r) // 2
            f = divide_conquer(nums,l,mid) 
            s = divide_conquer(nums,mid+1,r)
            ## not the same majority substract the extra
            if f[0] != s[0] :
                if f[1] > s[1] :
                    return (f[0],f[1]-s[1])
                else :
                    return (s[0],s[1]-f[1])
            else :
                return (f[0],s[1]+f[1])
        # print(divide_conquer(nums))
        n = len(nums)
        return divide_conquer(nums,0,n-1)[0]
         
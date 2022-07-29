from typing import List
import sys
class Solution:
    def _return(self, nums3):
        L = len(nums3)
        if (L%2) == 1:
            return nums3[L//2]

        return sum(nums3[L//2-1:L//2+1])/2
        
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0 :
            return self._return(nums2)
        elif len(nums2) == 0 :
            return self._return(nums1)
        L = (len(nums1)+len(nums2))

        l_count = 0
        l_iter = iter(nums1)
        l_max = len(nums1)
        l = next(l_iter)
        
        r_count = 0
        r_iter = iter(nums2)
        r_max = len(nums2)
        r = next(r_iter)
        
        nums3 = []
        
        for i in range(L):
            if l <= r:
                nums3.append(l)
                l_count += 1
                if l_count == l_max :
                    l = sys.maxsize
                else :
                    l = next(l_iter)
                
            else :
                nums3.append(r)
                r_count += 1
                if r_count == r_max :
                    r = sys.maxsize
                else :
                    r = next(r_iter)
        print(nums3)
        return self._return(nums3)
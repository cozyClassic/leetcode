class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        if buckets == 1:
            return 0
        pigs = 1
        trial = minutesToTest//minutesToDie
        
        for i in range(100):
            if (trial+1) ** pigs >= buckets:
                return pigs
            pigs +=1
            
        
        return count
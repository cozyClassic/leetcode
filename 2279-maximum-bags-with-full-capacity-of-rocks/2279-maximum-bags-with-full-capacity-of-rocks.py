class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        empties = [c-r for c,r in zip(capacity,rocks)]
        print(empties)
        empties.sort()
        
        result = 0
        
        for e in empties:
            if additionalRocks < e:
                return result
            additionalRocks -= e
            result += 1
        return result
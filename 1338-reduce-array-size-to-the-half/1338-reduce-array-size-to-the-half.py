from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        result = 0
        goal = len(arr) // 2
        print(goal)
        counter = Counter(arr)
        for num, count in counter.most_common():
            result += 1
            goal -= count
            if goal <= 0:
                break
            
        return result
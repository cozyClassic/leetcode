from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(list(s))
        answer = 10**5+1
        for key in counter :
            if  counter[key] == 1 and s.index(key) < answer :
                answer = s.index(key)
        
        return answer if answer != 10**5+1 else -1
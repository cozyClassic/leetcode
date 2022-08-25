from collections import Counter
class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        return Counter(r) == Counter(r)&Counter(m)
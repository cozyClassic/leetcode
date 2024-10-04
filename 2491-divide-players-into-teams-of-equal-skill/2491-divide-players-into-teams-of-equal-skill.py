from collections import Counter
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)

        target = 2 * sum(skill) / n
        if target % 1 != 0: return -1
        counts = Counter(skill)
        ans = 0
        for s, c in counts.items():
            if target - s not in counts: return -1
            if c != counts[target - s]: return -1
            total_chem = int(s * (target - s) * c)
            ans += total_chem
        return ans >> 1
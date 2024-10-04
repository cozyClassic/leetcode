from collections import deque

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) == 2: return skill[0] * skill[1]

        skill = deque(sorted(skill))
        result = 0
        standard = skill[0] + skill[-1]

        while skill:
            if skill[0] + skill[-1] != standard: return -1
            result += skill[0] * skill[-1]
            skill.popleft()
            skill.pop()

        return result
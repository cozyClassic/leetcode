class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) == 2: return skill[0] * skill[1]

        skill.sort()
        result = 0
        standard = skill[0] + skill[-1]
        L = len(skill) - 1

        for i in range((L+1)//2):
            if skill[i] + skill[L-i] != standard: return -1
            result += skill[i] * skill[L-i]

        return result
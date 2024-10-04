class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) == 2: return skill[0] * skill[1]

        skill.sort()
        result = 0
        standard = skill[0] + skill[-1]

        for i in range(len(skill)//2):
            if skill[i] + skill[len(skill)-i-1] != standard: return -1
            result += skill[i] * skill[len(skill)-i-1]

        return result
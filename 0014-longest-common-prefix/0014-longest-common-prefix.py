class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        word1 = strs[0]
        for word2 in strs:
            for i, (w1,w2) in enumerate(zip(word1, word2)):
                if w1 != w2:
                    word1 = word1[:i]
                    break
            else:
                word1 = word1[:min(len(word1), len(word2))]
        
        return word1
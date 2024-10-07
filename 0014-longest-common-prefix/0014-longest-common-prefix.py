class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort(key=lambda x : len(x))
        result = strs[0]        
        for word in strs : 
            for i in range(len(result)) :
                if result[i] != word[i] :
                    result = result[:i]
                    break
        
        return result
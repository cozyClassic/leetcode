class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphas = list("abcdefghijklmnopqrstuvwxyz")
        mors = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        a_to_m = {}
        for a,m in zip(alphas,mors):
            a_to_m[a] = m
        
        result = []
        for word in words :
            this = ""
            for w in word:
                this += a_to_m[w]
            result.append(this)
        
        return len(set(result))
class Solution:
    from collections import Counter
    VOWEL = {
        "a": ["e","i","u"],
        "e": ["a","i"],
        "i": ["e","o"],
        "o": ["i"],
        "u": ["i","o"]
    }
    def trans_char_nums(self,counter):
        new_counter = Counter()
        for V in self.VOWEL :
            for v in self.VOWEL[V]:
                new_counter[V] += counter[v]
        return new_counter        
        
    def countVowelPermutation(self, n: int) -> int:
        if n == 1 :
            return 5
        elif n == 2:
            return 10
        
        counter = Counter()
        for v in self.VOWEL:
            counter[v] = 1
        
        for i in range(2,n+1):
            counter = self.trans_char_nums(counter)
            
        answer = sum([counter[v] for v in counter])
        
        return answer % (10**9 + 7)
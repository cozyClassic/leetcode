class Solution:
    def get_list_len(self, words: List[str]) -> int:
        return sum([len(w) for w in words]) + len(words) - 1
    
    def get_a_line(self, words: List[str], maxWidth:int) -> str:
        if len(words) == 1:
            return words[0] + " " * (maxWidth - len(words[0]))
        min_space, last = divmod(maxWidth - sum([len(w) for w in words]),(len(words) - 1))
        line = ""
        for w in words[:-1]:
            line += w + " " * min_space
            if last > 0:
                line += " "
                last -= 1
        
        return line + words[-1]

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        L = len(words)
        
        curr = []
        i = 0

        while i < L:
            if len(curr) == 0:
                curr.append(words[i])
                i += 1
                continue
            # case1. 단어 추가
            if self.get_list_len(curr) + len(words[i]) + 1 <= maxWidth:
                curr.append(words[i])
                i += 1
            else:
                result.append(self.get_a_line(curr,maxWidth))
                curr = []
        if curr:
            word = " ".join(curr)
            word += " " * (maxWidth - len(word))
            result.append(word)
        return result
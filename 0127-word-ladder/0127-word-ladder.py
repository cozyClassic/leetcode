from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 방문 여부 체크
        word_to_sec = {}
        Q = deque()
        Q.append((beginWord, 1))
        wordList = set(wordList)

        while Q:
            word, sec = Q.popleft()
            if word in word_to_sec:
                continue
            word_to_sec[word] = sec
            for i in range(len(word)):
                 for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        Q.append((next_word, sec+1))

        return word_to_sec[endWord] if endWord in word_to_sec else 0
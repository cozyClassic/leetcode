"""
1. 서로 다른 문자의 개수 diff를 구하는 함수를 만든다.
2. diff가 1이면 변경 가능
3. diff를 기반으로 ChangeAble Map을 만든다.
4. BFS를 시전한다.
5. endGame에 해당하는 값이 보이면 return
6. return -1
"""
from collections import deque
class Solution:
    def is_mutable(self, A, B) -> bool:
        diff = 0
        for a,b in zip(A,B):
            if a != b:
                diff += 1
        return diff == 1
        
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_to_count = {}
        
        Q = deque()
        Q.append([startGene,0])
        while Q:
            gene, count = Q.popleft()
            if gene in bank_to_count:
                continue
            bank_to_count[gene] = count
            for other_gene in bank:
                if self.is_mutable(gene, other_gene):
                    if other_gene == endGene:
                        return count+1
                    Q.append([other_gene, count+1])
        return -1
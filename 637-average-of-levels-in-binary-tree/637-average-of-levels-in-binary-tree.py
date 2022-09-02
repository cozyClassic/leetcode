from collections import defaultdict, deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        results = {} # depth : sum, count
        Q = deque()
        Q.append((root, 0))
        
        while Q :
            node,depth = Q.popleft()
            if not node :
                continue
            
            if not depth in results :
                results[depth] = [0,0]
            
            results[depth][0] += node.val
            results[depth][1] += 1
            
            Q.append((node.left,depth+1))
            Q.append((node.right,depth+1))
        
        return [results[x][0]/results[x][1] for x in results]
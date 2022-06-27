class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        results = []
        goal = len(graph) - 1
        
        def dfs(n, route):            
            if n == goal :
                results.append(route)
                return
            nexts = graph[n]
            
            for _next in nexts:
                if _next in route:
                    return
                dfs(_next, route[:] + [_next])
        
        dfs(0, [0])
        
        return results
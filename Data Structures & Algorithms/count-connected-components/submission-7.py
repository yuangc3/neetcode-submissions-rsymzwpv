class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}

        visit = set()
        count = 0
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        

        def dfs(crs):
            visit.add(crs)

            for nei in adj[crs]:
                if nei not in visit:
                    dfs(nei)
        
        for i in range(n):
            if i not in visit:
                count += 1
                dfs(i)
        return count
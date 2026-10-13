class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return False
        adj = {i:[] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        def dfs(crs, prev):
            if crs in visited:
                return False
            
            visited.add(crs)
            for pre in adj[crs]:
                if pre == prev:
                    continue
                if not dfs(pre, crs):
                    return False
            return True
        return dfs(0, -1) and n == len(visited)


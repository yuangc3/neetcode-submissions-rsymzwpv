class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i :[] for i in range(n)}

        for s, e in edges:
            adj[s].append(e)
            adj[e].append(s)
        visit = set()
        def dfs(crs, parent):
            if crs in visit:
                return False
            visit.add(crs)
            for nei in adj[crs]:
                if nei == parent:
                    continue
                if not dfs(nei, crs):
                    return False
            return True
        if not dfs(0, -1):
            return False
        return len(visit) == n

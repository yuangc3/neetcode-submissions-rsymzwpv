class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n:
            return 0
        temp = {i:[] for i in range(n)}
        count = 0
        for u, v in edges:
            temp[u].append(v)
            temp[v].append(u)
        visited = set()

        def dfs(crs):            
            visited.add(crs)

            for pre in temp[crs]:
                if pre not in visited:
                    dfs(pre)
        

        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        return count 



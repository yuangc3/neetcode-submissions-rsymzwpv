class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #遍历所有节点。每当发现一个还没访问过的节点，就说明发现了一个新的 connected component，于是 count += 1，然后 DFS 把整个 component 标记为 visited。
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



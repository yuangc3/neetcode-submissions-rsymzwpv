class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}

        for start, pre in prerequisites:
            adj[start].append(pre)
        
        visit = set()
        def dfs(crs):
            if crs in visit:
                return False
            if adj[crs] == []:
                return True
            visit.add(crs)
            for nei in adj[crs]:
                if not dfs(nei):
                    return False
            visit.remove(crs)
            adj[crs] = []
            return True  
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}

        cycle, visit = set(), set()

        for s,p in prerequisites:
            adj[s].append(p)
        
        output = []
        def dfs(crs):
            if crs in visit:
                return True
            if crs in cycle:
                return False
            cycle.add(crs)
            for nei in adj[crs]:
                if not dfs(nei):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return output
        for i in range(numCourses):
            if not dfs(i):
                return []
        return output
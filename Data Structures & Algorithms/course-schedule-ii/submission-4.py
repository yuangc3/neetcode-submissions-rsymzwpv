class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}

        visit = set()
        cycle = set()
        for start, pre in prerequisites:
            adj[start].append(pre)
        output = []
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for prev in adj[crs]:
                if not dfs(prev):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return output
        for i in range(numCourses):
            if not dfs(i):
                return []
        return output
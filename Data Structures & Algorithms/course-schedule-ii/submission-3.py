class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {c:[] for c in range(numCourses)}
        output = []
        for crs, prev in prerequisites:
            preMap[crs].append(prev)
        
        visited, cycle = set(), set()

        def dfs(crs):
            if crs in visited:
                return True
            if crs in cycle:
                return False
            cycle.add(crs)
            for prev in preMap[crs]:
                if not dfs(prev):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return output
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output
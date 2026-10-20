class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i:[] for i in range(N)} #cost, node

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dis = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dis, j])
                adj[j].append([dis, i])
        minH = [[0, 0]] #cost, node
        visit = set()
        res = 0

        while len(visit) < N:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neicost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neicost, nei])
        return res

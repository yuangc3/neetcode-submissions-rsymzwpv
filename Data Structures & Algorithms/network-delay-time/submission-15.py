class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1, n+1)}
        heap = [(0, k)] #total time + node

        for u, v, t in times:
            adj[u].append((v, t)) #neighbor + time
        

        res = 0 
        visit = set()
        while heap:
            time, node = heapq.heappop(heap)
            if node in visit:
                continue
            visit.add(node)
            res = time
            for nei, weight in adj[node]:
                if nei not in visit:
                    heapq.heappush(heap, (weight+time, nei)) 
        if len(visit) == n:
            return res
        else:
            return -1


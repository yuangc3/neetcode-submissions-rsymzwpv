class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v,t)) #node, weight
        
        visit = set()
        res = 0 
        heap = [(0, k)] #weight,node

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


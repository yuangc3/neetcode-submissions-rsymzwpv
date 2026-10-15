class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        temp = {i:[] for i in range(1, n+1)}
        for u, v, t in times:
            temp[u].append([v, t])
        
        heap = [(0, k)]
        res = 0
        visited = set()
        while heap:
            time, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            res = time
            for nei, wei in temp[node]:
                if nei not in visited:
                    heapq.heappush(heap,(time+wei, nei))
        if len(visited) == n:
            return res
        else:
            return -1 


        
            
                


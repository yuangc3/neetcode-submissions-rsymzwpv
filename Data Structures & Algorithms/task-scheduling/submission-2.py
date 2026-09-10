class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = defaultdict(int)

        for t in tasks:
            count[t]+=1
        
        heap = []
        for cnt in count.values():
            heapq.heappush(heap, -cnt)
        
        time = 0

        q = deque()#storing [-cnt, idle_time]

        while heap or q:
            time += 1
            if heap:
                cnt = 1+heapq.heappop(heap)
                if cnt != 0:
                    q.append([cnt, n+time])

            if q and q[0][1] == time:
                cnt, idle_time = q.popleft()
                heapq.heappush(heap, cnt)
        
        return time
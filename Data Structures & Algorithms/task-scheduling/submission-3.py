class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #queue = [-cnt, n+current time]
        #heap = [-cnt]
        # {a:3, b:1, c: 1}
        temp = defaultdict(int)
        heap = []
        for t in tasks:
            temp[t] += 1
        time = 0
        q = deque()

        for v in temp.values():
            heapq.heappush(heap, -v)
        
        while q or heap:
            time += 1
            if heap:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    q.append([cnt, n+time])
            if q and q[0][1] == time:
                cnt, idle_time = q.popleft()
                heapq.heappush(heap, cnt)
        return time
                


            
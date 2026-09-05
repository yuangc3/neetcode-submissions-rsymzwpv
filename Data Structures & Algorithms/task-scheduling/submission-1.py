class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        temp = defaultdict(int)
        for t in tasks:
            temp[t] += 1
        queue =deque() #store[-count, time]
        heap = []
        time = 0
        for count in temp.values():
            heapq.heappush(heap, -count)
        
        while heap or queue:
            time += 1
            if heap:
                count = 1+heapq.heappop(heap)
                if count:
                    queue.append([count, n+time])
            if queue and queue[0][1] == time:
                val = queue.popleft()[0]
                heapq.heappush(heap, val)
        return time

        

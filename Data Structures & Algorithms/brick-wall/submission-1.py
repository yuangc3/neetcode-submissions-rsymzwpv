class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        temp = defaultdict(int)
        count = 0 
        for r in wall:
            if len(r) == 1:
                count += 1
        
        if count == len(wall):
            return len(wall)


        for r in wall:
            total = 0 
            for b in r[:-1]:
                total += b
                temp[total] += 1 
                

        return len(wall) - max(temp.values())
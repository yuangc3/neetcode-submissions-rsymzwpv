class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l <= r:
            mid = (l+r) // 2
            total_hours = 0 
            for c in piles:
                total_hours += math.ceil(c/mid)
            
            if total_hours <= h:
                res = mid
                r = mid - 1
            else:
                l = mid+1
        return res 


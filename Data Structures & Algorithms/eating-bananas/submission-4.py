class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 0
        while l <= r:
            mid = (l + r) // 2
            total_hour = 0
            for c in piles:
                total_hour += math.ceil(c / mid)

            if total_hour <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

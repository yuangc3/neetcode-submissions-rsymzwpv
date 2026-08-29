class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []

        for n in nums1:
            res.append(n)
        for n in nums2:
            res.append(n)
        
        res.sort()

        n = len(res)
        if n % 2 == 1:
            return res[n//2]
        else:
            total = res[n//2-1]+res[n//2]
            return total / 2

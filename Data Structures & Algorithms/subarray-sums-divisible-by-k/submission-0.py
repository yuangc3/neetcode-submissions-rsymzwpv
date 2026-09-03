class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        temp = defaultdict(int)
        temp[0] = 1 
        prefix = 0
        count = 0

        for num in nums:
            prefix += num
            remainder = prefix % k

            if remainder in temp:
                count += temp[remainder]

            temp[remainder]+=1
        return count
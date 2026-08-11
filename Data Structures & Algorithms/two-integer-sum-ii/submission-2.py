class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) -1 
        res = []
        while l <r:
            total = numbers[l] + numbers[r]
            if total == target:
                res.append(l+1)
                res.append(r+1)
                break
            if total < target:
                l+= 1
            else:
                r -= 1
        return res 
            
            

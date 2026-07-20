class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums) - 1
        jumps = 0

        while goal > 0:
            for i in range(goal):
                if i + nums[i] >= goal:
                    goal = i
                    jumps += 1
                    break

        return jumps

            
            
#2, 4, 1, 1, 1, 1
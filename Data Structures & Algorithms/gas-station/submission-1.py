class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur_gas = 0
        index = 0 
        if sum(gas) < sum(cost):
            return -1
        for i in range(len(gas)-1):
            cur_gas += (gas[i] - cost[i])
            if cur_gas < 0:
                cur_gas = 0
                index = i+1
        return index


        
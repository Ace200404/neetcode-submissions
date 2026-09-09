class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        
        total=0
        result=0
        for i in range(len(gas)):
            if total<0:
                total=0
                result=i
            total+=gas[i]-cost[i]
        return result
        
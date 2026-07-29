class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minValue=101
        total=0
        for i in prices:
            if i<minValue:
                minValue=i
            else:
                total=max(i-minValue,total)
        return total

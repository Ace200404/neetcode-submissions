class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit=0
        min_number=prices[0]

        for i in prices[1:]:

            if i<min_number:
                min_number=i
            else:
                profit=max(profit, i-min_number) 
            
        return profit 
            

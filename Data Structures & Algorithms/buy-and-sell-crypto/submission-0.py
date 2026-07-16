class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        a, b = 0,1 #set our pointer start position
        max_profit = 0 #set current profit to 0

        while b < len(prices): #keep b bounded
            if prices[a] < prices[b]: #if selling yeilds profit
                max_profit = max(max_profit, prices[b] - prices[a])#calculate new profit and see whether it is the max
            else:
                a = b #we only move a if measured gap has less than or equal to 0 profit
            b += 1 #move b along to look further into the future
        
        return max_profit #give answer
      

        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        f, l = 0, 1
        profit = 0

        while l < len(prices):
            if prices[f] < prices[l]:
                profit = max(profit, prices[l] - prices[f])
            else:
                f = l
            l += 1
        return profit


            
      

        
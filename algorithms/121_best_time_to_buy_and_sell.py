# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        profit = 0
        max_profit = 0
        
        for i in range(0, len(prices)):
            for j in range(i+1, len(prices)):
                
                profit = prices[j] - prices[i]
                
                if profit > max_profit:
                    max_profit = profit
                    
        return max_profit
        

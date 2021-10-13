# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        min_price = float('inf')
        max_profit = 0
        
        for i in range(0, len(prices)):
            
            if prices[i] < min_price:
                min_price = prices[i]
            
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        
        return max_profit

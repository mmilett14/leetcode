class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        min_price = float('inf')
        min_price_spot = 0
        
        max_price = float('inf')
        max_price_spot = 0
        
        
        for i in range (0, len(prices)):
            
            spot = i+1
            
            if (prices[i] < min_price) & (spot < max_price_spot):
                min_price = prices[i]
                min_price_spot = spot
                
            elif (prices[i] > max_price) & (spot > min_price_spot):
                max_price = prices[i]
                max_price_spot = spot
                
        
        return (max_price - min_price)
            

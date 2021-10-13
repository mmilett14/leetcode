# Need to address cases where the price is listed more than once

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        prices_asc = prices.copy()
        prices_asc.sort(reverse=False)
        
        prices_desc = prices.copy()
        prices_desc.sort(reverse=True)
        
        price_dict = {}
        
        profit = 0
        
        for i in range(0, len(prices)):
            
            price_dict[prices[i]] = i
            
        
        for i in range (0, len(prices)):
            
            for j in range (0, len(prices)):
            
                if (price_dict[prices_desc[i]] > price_dict[prices_asc[j]]) and ((prices_desc[i] - prices_asc[j]) > profit):
                    profit = (prices_desc[i] - prices_asc[j])
            
        return profit
        
        

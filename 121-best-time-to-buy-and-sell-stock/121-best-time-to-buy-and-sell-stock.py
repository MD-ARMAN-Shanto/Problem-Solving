class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = prices[0]
        profit = 0
        
        for i in range(1, len(prices)):
            
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                diff = prices[i] - min_price
                
                if diff > profit:
                    profit = diff
                    
        return profit
    
            
            

    
            
            
            
        
                
                
                
                    
                    
                    
        
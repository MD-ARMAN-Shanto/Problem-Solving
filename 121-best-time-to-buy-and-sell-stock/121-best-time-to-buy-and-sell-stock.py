class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        # for i_price in range(len(prices)):
        #     for f_price in range(i_price+1, len(prices)):
        #         diff = 0
        #         if prices[f_price] < prices[i_price]:
        #             continue
        #         else: 
        #             diff = prices[f_price] - prices[i_price] 
        #             if total < diff:
        #                 total = diff
        # return total
        
        min_price = prices[0]
        profit = 0
        
        for price in range(1, len(prices)):
            
            if prices[price] < min_price:
                min_price = prices[price]
            else:
                diff = prices[price] - min_price
                
                if profit < diff:
                    profit = diff
                
        return profit
            
            
            
        
                
                
                
                    
                    
                    
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = prices[0]
        profit = 0
        
        for price in range(1, len(prices)):

            if prices[price] < min_price:
                min_price = prices[price]
            else:
                diff = prices[price] - min_price 
                profit += diff
                min_price = prices[price]

        return profit
            
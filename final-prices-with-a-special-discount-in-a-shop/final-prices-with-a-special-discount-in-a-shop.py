class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        res = []
        
        for price in range(len(prices)):
            iPrice = prices[price]
            for discount in range(price+1, len(prices)):
                dPrice = prices[discount]
                
                if dPrice <= iPrice:
                    diff = iPrice - dPrice
                    res.append(diff)
                    break
            else:
                res.append(prices[price])
        
        return res
                
        
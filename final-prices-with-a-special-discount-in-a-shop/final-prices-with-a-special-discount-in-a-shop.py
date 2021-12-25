class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        res = []
        
        for price in range(len(prices)):
            iPrice = prices[price]
            for discount in range(price+1, len(prices)):
                dPrice = prices[discount]
                
                if dPrice <= iPrice:
                    res.append(iPrice - dPrice)
                    break
            else:
                res.append(iPrice)
        
        return res
                
        

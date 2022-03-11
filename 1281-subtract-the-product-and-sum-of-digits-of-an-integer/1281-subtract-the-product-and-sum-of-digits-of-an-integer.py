class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        product = 1
        total = 0
        
        while n:
            m = n % 10
            n //= 10
            product *= m
            total += m
            
        return (product-total)
            
        
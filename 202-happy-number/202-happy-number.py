class Solution:
    def isHappy(self, n: int) -> bool:
        
        visited = set()
        
        while n not in visited:
            
            visited.add(n)
            
            n = self.squareSum(n)
            
            if n == 1:
                return True
        return False
    
    def squareSum(self, n:int) -> int:
        
        count = 0
        
        while n:
            digit = n % 10
            count += digit * digit
            n //= 10
            
        return count

            
        

                
            
        
        
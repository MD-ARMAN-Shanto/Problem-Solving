class Solution:
    def addDigits(self, num: int) -> int:
        
        count = 0

        while num > 0:
            
            m = num % 10
            count += m
            num //= 10
            
            if num == 0 and count > 9:
                num = count
                count = 0
                    
        return count
                
            
            
        
        
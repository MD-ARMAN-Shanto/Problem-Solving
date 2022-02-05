class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n == 1:
            return True
        
        if n == 0:
            return False
        
        while  n % 2 == 0: 
            
            n /= 2
        
        return True if int(n) == 1 else False
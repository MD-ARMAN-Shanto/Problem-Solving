class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        # recursion process
        if n == 1:
            return True
        
        if n % 2 != 0 or n == 0:
            return False
        
        return self.isPowerOfTwo(n/2)
    
        # iterative process

        if n == 1:
            return True
        
        if n == 0:
            return False
        
        while  n % 2 == 0: 
            
            n /= 2
        
        return True if int(n) == 1 else False

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        # recursion solution
        if n == 1:
            return True
        
        if n % 3 != 0 or n == 0:
            return False
        
        return self.isPowerOfThree(n/3)
    
        # iterative solution
        
        if n == 1:
            return True
        
        if n == 0:
            return False
        
        while n % 3 == 0:
            
            n /= 3
            
        return True if int(n) == 1 else False
        

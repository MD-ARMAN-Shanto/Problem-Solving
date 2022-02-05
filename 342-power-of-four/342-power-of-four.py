class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        # recursion solution
        if n == 1:
            return True
        
        if n % 4 != 0 or n == 0:
            return False
        
        return self.isPowerOfFour(n/4)
    
        # iterative solution
        
        if n == 1:
            return True
        
        if n == 0:
            return False
        
        while n % 4 == 0:
            n /= 4
        
        return True if int(n) == 1 else False

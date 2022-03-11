class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        b_n = bin(n)[2:]
        
        
        for i in range(1, len(b_n)):
            
            i_b = b_n[i-1] #inital it
            c_b = b_n[i]   #current bit
            
            if i_b == c_b:
                return False
            
        return True
                
        
        
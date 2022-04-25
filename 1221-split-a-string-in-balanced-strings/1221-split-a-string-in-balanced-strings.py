class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        res = count = 0
        for i in range(len(s)):
            
            if s[i] == 'L':
                count += 1
            elif s[i] == 'R':
                count -= 1
            res += count == 0
                 
        return res
                
        
            
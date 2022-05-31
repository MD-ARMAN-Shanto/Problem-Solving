class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        i, j = 0, 0
        count = 0
        d = dict()
        
        while j < len(s):  
            
            d[s[j]] = d.get(s[j], 0) + 1
                
            if j - i + 1 < 3:
                j += 1
            
            elif j - i + 1 == 3:
                
                if len(d) == 3:
                    count += 1
                    
                d[s[i]] -= 1

                if d[s[i]] == 0:
                    d.pop(s[i])
                
                i += 1
                j += 1
                
        return count
                
                    
            
            
        
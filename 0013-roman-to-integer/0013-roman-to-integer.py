class Solution:
    def romanToInt(self, s: str) -> int:
        
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        num = 0

        for i in range(len(s)-2, -1, -1):
            curr_int = d[s[i]]
            prev_int = d[s[i+1]]
            
            if curr_int < prev_int:
                val = curr_int
                num -= val
                continue
                    
            else:
                val = curr_int 
                num += val
            
        return num + d[s[len(s)-1]]
                
            
            
            
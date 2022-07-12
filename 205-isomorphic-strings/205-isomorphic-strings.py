class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        d = {}
        se = set()
        
        
        for i in range(len(s)):
            x = s[i]
            y = t[i]
            
            if x not in d:
                if y in se:
                    return False
                d[x] = y
                se.add(y)
            else:
                if d[x] != y:
                    return False
                
        return True
                        
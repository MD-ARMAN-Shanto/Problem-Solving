class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        
        l = s.split(' ')
        
        if len(p) != len(l):
            return False
        
        d = {}
        se = set()
        
        for i in range(len(l)):
            x = p[i]
            y = l[i]
            
            if x not in d:
                if y in se:
                    return False
                d[x] = y
                se.add(y)
                
            else:
                if d[x] != y:
                    return False
                
        return True

        
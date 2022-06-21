class Solution:
    def sortString(self, s: str) -> str:
        
        s = list(s)
        result = []
        
        while len(s) > 0:
            
            smallest = sorted(set(s))
            
            for small in smallest:
                result.append(small)
                s.remove(small)
                
            biggest = sorted(set(s), reverse=True)
            
            for big in biggest:
                result.append(big)
                s.remove(big)
                
        return ''.join(result)
        
        
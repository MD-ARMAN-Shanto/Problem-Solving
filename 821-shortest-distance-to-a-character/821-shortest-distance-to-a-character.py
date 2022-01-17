class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        
        occurance = []
        
        for i in range(len(s)):
            if s[i] == c:
                occurance.append(i)
        _ = []
        res = []
        for ch in range(len(s)):
            for r in occurance:
                min_val = abs(r-ch)
                _.append(min_val)
                # res.append(min(abs(r-ch) for r in occurance))
            res.append(min(_))
            _[:] = []
                
        return res
        
        
        occurance = []
        
        for i in range(len(s)):
            if s[i] == c:
                occurance.append(i)

        res = []
        for ch in range(len(s)):
            res.append(min(abs(r-ch) for r in occurance))
                
        return res
            
            
        

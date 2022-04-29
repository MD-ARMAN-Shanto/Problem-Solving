class Solution:
    def secondHighest(self, s: str) -> int:
        li = list(s)
        s = list()
        
        for w in li:
            if w.isdigit():
                if w in s:
                    continue
                s.append(w)
        res = sorted(s, reverse=True)
        return int(res[1]) if len(s) > 1 else -1
                
        
                
            
        
        
        
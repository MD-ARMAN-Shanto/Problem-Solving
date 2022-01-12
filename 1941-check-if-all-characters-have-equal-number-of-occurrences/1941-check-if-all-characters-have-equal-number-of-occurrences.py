class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        
        d = {}
        
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1
        dic_val = list(d.values())[0]
        for i, v in d.items():
            if v != dic_val:
                return False
            
        return True
                
        
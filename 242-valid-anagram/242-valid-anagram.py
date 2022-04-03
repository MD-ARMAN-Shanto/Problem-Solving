class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        d = {}
        
        for ch in list(s):
            d[ch] = d.get(ch, 0) + 1
        
        
        for ch in list(t):
            if ch in d and d[ch] > 0: 
                d[ch] -= 1
            else:
                return False

        return True
        
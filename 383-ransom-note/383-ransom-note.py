class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        d = {}
        
        for ch in ransomNote:
            d[ch] = d.get(ch, 0) + 1
            
        for ch in magazine:
            if ch in d.keys():
                d[ch] -= 1
                if d[ch] == 0:
                    del d[ch]
        
        
        return True if len(d) == 0 else False        
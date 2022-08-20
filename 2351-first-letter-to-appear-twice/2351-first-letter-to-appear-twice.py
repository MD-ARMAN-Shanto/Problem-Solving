class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        xset = set()
        
        for ch in s:
            if ch in xset:
                return ch
            else:
                xset.add(ch)
                
                
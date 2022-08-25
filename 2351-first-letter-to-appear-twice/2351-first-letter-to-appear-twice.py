class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        xset = set()
        
        for ch in s:
            if not ch in xset:
                xset.add(ch)
            else:
                return ch
                
                
                
class Solution:
    def checkRecord(self, s: str) -> bool:
        
        a_count = 0
        l_count = 0
        
        for ch in reversed(range(len(s))):
            if s[ch] == "A":
                a_count += 1
            
        for ch in reversed(range(len(s)-2)):
            if s[ch] == "L":
                if s[ch] == s[ch+1] and s[ch+1] == s[ch+2]:
                    l_count = 3
        
        if a_count >= 2 or l_count >= 3:
            return False
        return True
            
        
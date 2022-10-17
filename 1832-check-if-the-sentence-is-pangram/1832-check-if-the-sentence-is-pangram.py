class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        s = set()
        
        for ch in sentence:
            if ch in s:
                continue
            else:
                s.add(ch)
                
        return True if len(s) == 26 else False
        
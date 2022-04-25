class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        res = []
        
        for word in words:
            ch = word[:len(pref)]
            res.append(ch)
        
        count = 0
        for ch in res:
            if ch == pref:
                count += 1
                
        return count
            
                
                
                
        
class Solution:
    def secondHighest(self, s: str) -> int:
        li = list()
        
        for w in range(len(s)):
            if s[w].isdigit():
                if s[w] in li:
                    continue
                li.append(s[w])
        res = sorted(li, reverse=True)
        return int(res[1]) if len(li) > 1 else -1
                
        
                
            
        
        
        
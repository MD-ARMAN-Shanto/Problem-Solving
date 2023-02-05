class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        i, j = 0, 0
        d = {}
        
        for word in p:
            d[word] = d.get(word, 0) + 1
            
        count = len(d)
        res = []
        
        while j < len(s):
            if s[j] in d:
                d[s[j]] -= 1
                if d[s[j]] == 0:
                    count -= 1

            if j - i + 1 < len(p):
                j += 1
            
            elif j - i + 1 == len(p):
                if count == 0:
                    res.append(i)
                    
                if s[i] in d:
                    d[s[i]] += 1
                    if d[s[i]] == 1:
                        count += 1
                i += 1
                j += 1
        
        return res
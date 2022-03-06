class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        d1, d2 = collections.defaultdict(int), collections.defaultdict(int)
        
        for word in s1.split(' '):
            if word not in d1:
                d1[word] = 1
            else:
                d1[word] += 1
                
        for word in s2.split(' '):
            if word not in d2:
                d2[word] = 1
            else:
                d2[word] += 1
        
        res = []
        for key in d1:
            if key not in d2:
                if d1[key] < 2:
                    res.append(key)
                
        for key in d2:
            if key not in d1:
                if d2[key] < 2:
                    res.append(key)
            
        return res
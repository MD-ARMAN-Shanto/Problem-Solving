class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        d = {}
        
        for word in words:
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1
        
        res = []
        while k > 0:
            max_key = max(sorted(d), key=d.get)
            del d[max_key]
            res.append(max_key)
            k -= 1
            
        return res
            
            
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        d = {}
        res = []
        
        for ch in arr:
            d[ch] = d.get(ch, 0) + 1
            
        for i, v in d.items():
            if i == v:
                res.append(i)
                
        return max(res) if len(res) != 0 else -1
        
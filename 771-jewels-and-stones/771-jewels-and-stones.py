class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        d = {}
        count = 0
        
        for st in stones:
            if st not in d:
                d[st] = 1
            else:
                d[st] += 1
        
        for je in jewels:
            if je in d:
                count += d[je]
                
        return count
        
        
        
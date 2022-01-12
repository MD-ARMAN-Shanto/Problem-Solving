class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        # solution 1 O(n^2)
        count = 0
        
        for i in range(len(stones)):
            for j in range(len(jewels)):
                if stones[i] == jewels[j]:
                    count += 1
            
            
        return count
        
        # solution 2 O(n)
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
        
        
        

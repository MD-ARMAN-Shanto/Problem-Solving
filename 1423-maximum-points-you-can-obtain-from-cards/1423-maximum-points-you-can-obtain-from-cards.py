class Solution:
    def maxScore(self, cp: List[int], k: int) -> int:
        
        N = len(cp)
        M = N-k
        total = sum(cp)
        mn = s = sum(cp[:M])
        
        for i in range(k):
            s -= cp[i]
            s += cp[i+M]
            mn = min(mn, s)
        
        return total - mn
            
            
            
            
                
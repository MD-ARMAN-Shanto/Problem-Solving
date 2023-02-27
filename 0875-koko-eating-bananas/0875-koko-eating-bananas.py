class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        lo, hi = 1, max(piles)
        res = hi
        
        while lo <= hi:
            mid = (lo+hi)//2
            hours = 0
            
            for p in piles:
                hours += math.ceil(p/mid)
                
            if hours <= h:
                res = min(res, mid)
                hi = mid -1
            else:
                lo = mid + 1
                
        return res
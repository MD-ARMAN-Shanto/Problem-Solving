class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        maxCandy = max(candies)
        res = []
        
        for i in range(len(candies)):
            total = candies[i] + extraCandies
            if total < maxCandy:
                res.append(False)
            else:
                res.append(True)
            
        return res
        
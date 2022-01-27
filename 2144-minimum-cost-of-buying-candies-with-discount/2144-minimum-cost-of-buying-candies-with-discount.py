class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        
        cost.sort(reverse=True)
        i , total, size = 0, 0, len(cost)
        
        while i < size:
            total += sum(cost[i: i+2])
            i += 3
        return total
            
            
                
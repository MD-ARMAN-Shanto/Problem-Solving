class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        
        # max_heap
        stones = [-val for val in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            f_val = heapq.heappop(stones)
            s_val = heapq.heappop(stones)
            
            if f_val < s_val:
                heapq.heappush(stones, f_val-s_val)
                
        if len(stones) < 1:
            return 0
        
        return -stones[0]
                
        
            
            
        
        
                
                
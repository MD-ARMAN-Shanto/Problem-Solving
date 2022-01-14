from heapq import heapify, heappush, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        res = []
        
        for i in range(len(nums)):
            
            heapq.heappush(res, nums[i])
            
            if len(res) > k:
                heapq.heappop(res)
            
        return res[0]
        
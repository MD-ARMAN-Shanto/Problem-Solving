class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        res = []
        
        for i in range(len(nums)):
            if nums[i] not in res:
                heapq.heappush(res, nums[i]) 
            if len(res) > 3:
                heapq.heappop(res)
        if len(res) < 3:
            return max(nums)
        
        return heapq.heappop(res)
        
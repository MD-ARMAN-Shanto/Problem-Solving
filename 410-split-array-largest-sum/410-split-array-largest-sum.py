class Solution:
                 
    def splitArray(self, nums: List[int], m: int) -> int:
        
        def canSplit(largest):
            subArray = 0
            curSum = 0

            for num in nums:
                curSum += num

                if curSum > largest:
                    subArray += 1
                    curSum = num

            return subArray + 1 <= m
    
        l, r = max(nums), sum(nums)
        res = r
        
        while l <= r:
            mid = l + ((r-l) // 2)
            
            if canSplit(mid):
                
                res = mid
                r = mid - 1
            else:
                l = mid + 1
                
        return res
                        
        
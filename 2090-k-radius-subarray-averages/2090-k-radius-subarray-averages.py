class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        left, s, radius = 0, 0, 2*k+1
        
        res = [-1] * len(nums)
        
        for right in range(len(nums)):
            s += nums[right]
            if (right - left + 1) >= radius:
                res[left+k] = s // radius
                s -= nums[left]
                left += 1
                
        return res
                
                
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        N = len(nums)
        result, minVal, maxVal = nums[0],  nums[0] ,  nums[0] 
        for i in range(1, N):
            tmp = maxVal
            maxVal = max(nums[i], tmp * nums[i], minVal * nums[i])
            minVal = min(nums[i], tmp * nums[i], minVal * nums[i])
            result = max(result, minVal, maxVal)
        return result
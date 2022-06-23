class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        total = sum(nums)
        leftMost = 0
        
        
        for i in range(len(nums)):
            rightSum = total - (nums[i] + leftMost)
            
            if leftMost == rightSum:
                return i
            
            leftMost += nums[i]
            
        return -1
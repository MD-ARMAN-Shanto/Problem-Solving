class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        max_num = 0
        
        for i in range(len(nums)):
            if nums[i] > nums[max_num]:
                max_num = i
                
        return max_num
        
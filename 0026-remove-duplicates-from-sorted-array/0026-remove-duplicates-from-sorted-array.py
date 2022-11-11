class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        for i in range(len(nums)-1, 0, -1):
            prev = nums[i-1]
            if prev == nums[i]:
                nums.pop(i)
            
        
        
        
                
        
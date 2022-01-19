class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = 0
        
        for num in range(len(nums)):
            
            if nums[num] != 0:
                nums[i], nums[num] = nums[num], nums[i]
                i += 1
                
        return nums


                
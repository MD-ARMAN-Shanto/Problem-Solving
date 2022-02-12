class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        for num in range(len(nums)-1, -1, -1):
            
            if nums[num] == val:
                nums.pop(num)
    
        return len(nums)
                
                
                
                
                
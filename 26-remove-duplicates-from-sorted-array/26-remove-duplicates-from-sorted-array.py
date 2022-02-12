class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # for i in range(len(nums)-1,0, -1):
        #     print(nums[i])
        #     if nums[i] == nums[i-1]:
        #         del nums[i]
        
        for i in range(len(nums)-1, 0, -1):
            prev = nums[i-1]
            curr = nums[i]
            if prev == curr:
                nums.pop(i)
                

        
        
        
                
        
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        # for num in nums:
        #     if original == num:
        #         original = num * 2
        #     for i in nums:
        #         if original == i:
        #             original = i * 2
        #             continue
        # return original 
        
        i = 0
        
        while i < len(nums):
            if nums[i] == original:
                original = nums[i] * 2
                i = 0
            else:
                i+=1
                
        return original
        
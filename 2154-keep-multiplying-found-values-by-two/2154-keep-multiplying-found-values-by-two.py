class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        # 1st approach
        # for num in nums:
        #     if original == num:
        #         original = num * 2
        #     for i in nums:
        #         if original == i:
        #             original = i * 2
        #             continue
        # return original 
        
        # 2nd approch
        # i = 0
        
        # while i < len(nums):
            # if nums[i] == original:
                # original = nums[i] * 2
                # i = 0
            # else:
                # i+=1
                
        # return original
        
        # 3rd approach
        nums = set(nums)
        
        while original in nums:
            original *= 2
        return original
    
    
        

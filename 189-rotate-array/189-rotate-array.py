class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
#         for num in range(k):
            
#             res = nums.pop(len(nums)-1)
            
#             nums.insert(0, res)
            
#         return nums

        k = k % len(nums)
    
        nums[:] = nums[-k:] + nums[:-k]
        
        return nums

    
        
        
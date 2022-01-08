class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
#         max_num = 0
        
#         for i in range(len(nums)):
#             if nums[i] > nums[max_num]:
#                 max_num = i
                
#         return max_num

        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start+end) // 2
            
            if nums[mid] > nums[mid+1]:
                end = mid 
            else:
                start = mid + 1
            
        return start
            
            
                

                
        
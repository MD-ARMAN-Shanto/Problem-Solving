class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        start = 0
        end = len(nums)-1
        
        while start < end:
            if nums[start] % 2 != 0 and nums[end] % 2 != 0:
                end -= 1
            elif nums[start] % 2 == 0 and nums[end] % 2 == 0:
                start += 1
            elif nums[start] % 2 == 0 and nums[end] % 2 != 0:
                end -= 1
            else:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        return nums
                
        
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        start = 0
        end = len(nums)-1
        f_p = -1
        
        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                f_p = mid
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
                
        l_p = -1
        low = 0
        high = len(nums)-1
        
        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                l_p = mid
                low = mid + 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
                
        return [f_p, l_p]
        
        
                   
                
                
        
                                
        
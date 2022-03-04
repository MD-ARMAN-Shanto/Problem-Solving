class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0 
        right = len(nums)
        l = len(nums)
        
        while left <= right:
            
            mid = (left + right) // 2
            
            if mid >= l:
                return -1
            
            if nums[mid] == target:
                return mid
            
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
                
        
        return -1
        
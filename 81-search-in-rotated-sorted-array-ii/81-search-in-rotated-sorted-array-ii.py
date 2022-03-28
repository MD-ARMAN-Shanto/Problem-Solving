class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        nums.sort()
        
        l = 0
        r = len(nums)-1 
        
        while l <= r:
            mid = (l+r)//2
            
            if nums[mid] == target:
                return True
            
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
                
        return False
        
        
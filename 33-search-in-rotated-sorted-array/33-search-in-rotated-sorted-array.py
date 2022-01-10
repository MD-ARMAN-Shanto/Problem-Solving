class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # time complexity O(n)
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            
        return -1
    
        # time complexity O(logn)
        l = 0
        h = len(nums)-1
        
        while l <= h:
            mid = (l+h) // 2
            
            if target == nums[mid]:
                return mid
            
            # left portion sorted array
            elif  nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    h = mid - 1
            # right portion sorted array
            else:
                if target < nums[mid] or target > nums[h]:
                    h = mid - 1
                else:
                    l = mid + 1
        return -1
                
                
                

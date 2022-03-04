class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # if target not in nums:
        #     nums.append(target)
        # return sorted(nums).index(target)
        
        # nums.append(target)
        # # nums.sort()
        # val = nums.index(target)
        # return val
        
        start = 0
        end = len(nums)-1
        
        while start <= end:
            mid = (start+end)//2
            
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                start = mid + 1 
            else:
                end = mid - 1
                
        return start 
                
        
            
        
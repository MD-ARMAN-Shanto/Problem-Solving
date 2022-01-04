class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)
        
        result = nums[0] + nums[1] + nums[len(nums)-1] # -3, -1, 0, 2
        
        for i in range(len(nums)-1):
            left = i + 1 # -1, 1
            right = len(nums)-1 # 2
            
            while left < right:
                current = nums[i] + nums[left] + nums[right] # -3, -1, 0, 2
                
                if current == target:
                    return target
                
                elif abs(target - current) < abs(target - result): # 1 < 1
                    result = current
                
                elif current > target:
                    right -= 1
                    
                elif current < target:
                    left += 1
                    
        return result
                    
            
            
            
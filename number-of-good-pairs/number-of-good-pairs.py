class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        count = 0
            
        for i in range(len(nums)): # i = 1
            for j in range(1, len(nums)): # j = 2
                if nums[i] == nums[j] and i < j:
                    count += 1
                    
        return count
        
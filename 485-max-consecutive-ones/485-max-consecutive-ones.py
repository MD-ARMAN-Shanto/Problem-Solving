class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        one = 0
        max_one = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                one += 1
            else:
                one = 0
            if one > max_one:
                max_one = one
                
        return max_one
        
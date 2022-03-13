class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        flag = 0
        
        for num in range(len(nums)):
            if nums[num] == 0:
                return 0
            elif nums[num] < 0:
                flag += 1
                
        return 1 if flag % 2 == 0 else -1
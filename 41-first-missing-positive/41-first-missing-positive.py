class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        d = {}
        
        for num in nums:
            if num not in d:
                d[num] = 1
        
        for i in range(1, len(nums)+3):
            if i not in d  and i>0:
                return i
                
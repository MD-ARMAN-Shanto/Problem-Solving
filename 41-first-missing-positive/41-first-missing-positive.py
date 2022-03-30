class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        s = set(nums)
        
        for i in range(1, len(nums)+3):
            if i not in s and i > 0:
                return i
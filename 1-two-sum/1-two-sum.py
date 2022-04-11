class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        values = {}
        
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in values:
                return [i, values[remaining]]
            else:
                values[num] = i
import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        res = 0
    
        for num in nums:
            res |= num
        return res * int(pow(2, len(nums)-1))


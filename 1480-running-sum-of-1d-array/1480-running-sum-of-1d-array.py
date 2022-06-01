class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        res = []
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            res.append(s)
        return res
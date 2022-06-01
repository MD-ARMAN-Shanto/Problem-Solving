class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        # res = [nums[i]*(nums[i]+1)/2 for i in range(len(nums)]
        res = []
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            res.append(s)
        return res
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        d = {}
        
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
        
        return min(d.keys(), key=d.get)
        
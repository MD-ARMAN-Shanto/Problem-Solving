class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        res = {}
        
        for num in range(len(nums)):
            val = nums[num]
            if nums[num] not in res:
                res[val] = 1
            else:
                res[val] += 1
        
        l = []
        
        for k, v in res.items():
            if v >  len(nums)//3:
                l.append(k)
        
        return l
        
        
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        
        # for num in range(len(nums)):
        #     initial_num = nums[num]
        #     for next_num in range(num+1, len(nums)):
        #         if initial_num == nums[next_num]:
        #             return initial_num
        
        res = {}
        
        for key, num in enumerate(nums):
            if num in res:
                res[num] += 1
            else:
                res[num] = 1
                
        return max(res, key=res.get)
            
        
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
#         count = 0
#         res = []
        
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if j != i and nums[j] < nums[i]:
#                     count += 1
#             res.append(count)
#             count = 0
        

        len_nums = len(nums)
        sorted_items = sorted(nums)
        dic = dict()
        res = list()
        
        for i in range(len_nums):
            if sorted_items[i] not in dic:
                dic[sorted_items[i]] = i
            else:
                continue

        for i in range(len_nums):
            res.append(dic[nums[i]])
                
                
        return res
                
            
            
        
        
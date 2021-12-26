class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
#         li = [[]]
#         total = 0
        
#         for i in range(len(nums)+1):
#             for j in range(i):
#                 li.append(nums[j:i])
        
#         print(li)

        res = 0
    
        for num in nums:
            res |= num
        return res * int(pow(2, len(nums)-1))
        
                

                
            
        
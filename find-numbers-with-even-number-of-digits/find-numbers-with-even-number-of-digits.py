class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
#         res = []
#         target = 1
        
#         for num in nums:
#             count = 0
            
#             while(num != 0):
#                 num = num // 10
#                 count += 1
#             if count % 2 == 0:
#                 res.append(target)
#                 target+=1
            
                
#         return len(res)

        arr = []
        count = 0
        for num in nums:
            res = floor(log10(num) + 1)
            if res % 2 == 0:
                arr.append(count)
                count+=1
        return len(arr)
                
        
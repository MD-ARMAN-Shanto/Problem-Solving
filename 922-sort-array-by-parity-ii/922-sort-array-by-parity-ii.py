class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        
#         even_arr = []
#         odd_arr = []
        
#         for i in range(len(nums)):
#             if nums[i] % 2 == 0:
#                 even_arr.append(nums[i])
#             else:
#                 odd_arr.append(nums[i])
                
#         res = []
#         for j in range(len(even_arr)):
#             res.append(even_arr[j])
#             res.append(odd_arr[j])
            
#         return res

        j = 1
        for i in range(0, len(A), 2):
            if A[i] % 2:
                while A[j] % 2:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A
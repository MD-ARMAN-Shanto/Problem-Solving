class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
#         start = 0
#         end = len(numbers) - 1
        
#         while start < end:
#             pointer_addition = numbers[start] + numbers[end]
#             if  pointer_addition == target:
#                 return [start+1, end+1]
#             elif target > pointer_addition:
#                 start += 1
#             else:
#                 end -= 1
                
        values = {}

        for i, num in enumerate(numbers):
            remaining = target - num
            if remaining in values:
                return [values[remaining], i+1]
            else:
                values[num] = i+1
        
        return []
                
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
#         start = 0
#         end = len(heights) - 1
#         count = 0
        
#         while start < end:
            
#             if heights[start] < heights[end]:
#                 start += 1
#             else:
#                 heights[start], heights[end] = heights[end], heights[start]
#                 end -= 1
#                 count += 1
        
        
#         print(heights, count)


        duplicate = sorted(heights)
        count = 0
        
        for i, j in zip(heights, duplicate):
            
            if i != j:
                count += 1
                
        return count
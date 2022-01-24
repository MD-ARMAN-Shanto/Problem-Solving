class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # approch 1 builtin stl method
        # return sorted(nums)
        
        # approch 2 priority queue
        
        h = []
        res = []
        for value in nums:
            heapq.heappush(h, value)
        
        return [heapq.heappop(h) for i in range(len(h))]
    
        # approch 3 using recursion for small length

#         if len(nums) == 0:
#             return
        
#         temp = nums[-1]
#         nums.pop()
        
#         self.sortArray(nums)
#         self.insertSort(nums, temp)
        
#         return nums
        
#     def insertSort(self, arr: List[int], temp: int):
        
#         if len(arr) == 0 or temp >= arr[-1]:
#             arr.append(temp)
#             return
        
#         tmp = arr[-1]
#         arr.pop()
        
#         self.insertSort(arr, temp)
#         arr.append(tmp)
        
        
        
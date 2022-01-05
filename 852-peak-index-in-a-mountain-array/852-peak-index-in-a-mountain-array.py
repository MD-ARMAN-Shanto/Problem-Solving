class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        
        for num in range(1, len(arr)):
            prev = arr[num-1]
            current_num = arr[num]
            
            if prev < current_num:
                continue
            else:
                return num - 1
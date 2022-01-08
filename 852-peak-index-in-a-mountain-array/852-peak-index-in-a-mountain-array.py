class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        # 1st approch
        # complexity O(n)
        for num in range(1, len(arr)):
            prev = arr[num-1]
            current_num = arr[num]
            
            if prev < current_num:
                continue
            else:
                return num - 1
            
        # approch 2 
        # complexity O(logn)
        start = 0
        end = len(arr) - 1
        mid = (start+end) // 2
        while start <= end:
            if arr[mid] >= arr[mid+1]:
                end = mid - 1
            else:
                start = mid + 1
            
            mid = (start+end) // 2
            
        return mid+1
    
        # approch 3
        start = 0
        end = len(arr) - 1

        while start < end:
            mid = (start+end) // 2
            if arr[mid] > arr[mid+1]:
                end = mid 
            else:
                start = mid + 1
            
        return start


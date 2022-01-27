class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        arr.sort()
        res = []
        
        min_diff = abs(arr[0]-arr[1])
        
        for i in range(1, len(arr)):
            prev = arr[i-1]
            curr = arr[i]
            
            min_diff = min(abs(prev-curr), min_diff)
            
        
        for j in range(1, len(arr)):
            
            if abs(arr[j-1] - arr[j]) == min_diff:
                res.append([arr[j-1], arr[j]])
                
        return res
            
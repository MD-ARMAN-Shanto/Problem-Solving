class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        arr.sort()
        diff = arr[1] - arr[0]
        
        for i in range(2, len(arr)):
            prev = arr[i-1]
            curr = arr[i]
            
            difference = curr - prev
            
            if diff != difference:
                return False
        
        return True
            
        
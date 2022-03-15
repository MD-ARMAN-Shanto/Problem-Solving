class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        total = 0
        # print(len(arr))
        
        for i in range(len(arr)+1):
            if i % 2 == 0:
                continue
            
            indx = 0
            
            while indx + i <= len(arr):
                total += sum(arr[indx:indx+i])
                indx += 1
                
            # for j in range(i, len(arr),2):
                # total += sum(arr[i:j+1])
                
        return total
                
            
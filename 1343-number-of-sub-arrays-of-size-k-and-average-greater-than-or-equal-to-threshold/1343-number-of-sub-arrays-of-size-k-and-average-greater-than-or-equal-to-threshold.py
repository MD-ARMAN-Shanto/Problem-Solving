class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        i, j = 0, 0
        total = 0
        count = 0
        
        while j < len(arr):
            total += arr[j]
            
            if j - i + 1 < k:
                j += 1
            
            elif j - i + 1 == k:
                avg = total//k
                if avg < threshold:
                    total -= arr[i]
                    i += 1
                    j += 1
                    continue
                else:
                    count += 1
                total -= arr[i]
                i += 1
                j += 1
                
        
        return count
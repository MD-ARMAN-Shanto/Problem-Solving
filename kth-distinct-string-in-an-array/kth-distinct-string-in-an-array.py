class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        hashMap = {}
        count = 0
        res = []
        
        for ch in range(len(arr)):
            
            if arr[ch] not in hashMap:
                hashMap[arr[ch]] = 1
            else:
                hashMap[arr[ch]] += 1
        
        
        for key, value in hashMap.items():
            if value == 1:
                res.append(key)
                
        if k > len(res):
            return ""
        return res[k-1]
            
            
            
            
        
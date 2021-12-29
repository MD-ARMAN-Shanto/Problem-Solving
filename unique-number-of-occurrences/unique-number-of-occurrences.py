class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        res = {}
        
        for i in range(len(arr)):
            
            if arr[i] not in res:
                res[arr[i]] = 1
            else:
                res[arr[i]] += 1

        setVal = len(set(res.values()))
        
        if len(res) != setVal:
            return False
        return True
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        d = {}
        
        for ch in list(s):
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] -= 1
        
        first_value = ""
        for i, k in d.items():
            if k == 1:
                first_value = i
                break
        
        li = list(s)
        
        for i in range(len(li)):
            print(li[i])
            if li[i] == first_value:
                return i
                break
        
        return -1
        
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        l1 = list(s)
        
        for i in range(len(t)):
            if t[i] in l1:
                l1.remove(t[i])
            else:
                return t[i]
                    
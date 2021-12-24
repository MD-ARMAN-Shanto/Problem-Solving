class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        
        res = []
        temp = 0
        end = len(s) - 1

        for i in range(len(s)):
            if s[i] == 'I':
                res.append(temp)
                temp += 1
            else:
                res.append(end + 1)
                end -= 1
        res.append(end + 1)
        return res                
                
        
class Solution:
    def replaceDigits(self, s: str) -> str:
        res = []
        
        for i in range(len(s)):
            if s[i].isdigit():
                val = ord(s[i - 1]) + int(s[i])
                res.append(chr(val))
                continue
            else:
                res.append(s[i])
        
        return ''.join(res)
        
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:

        s = 0
        for n in num:
            s *= 10
            s += n
            
        return [int(x) for x in str(s+k)]
            
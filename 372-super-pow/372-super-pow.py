
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        
        mod = 1337
        
        num = ''.join([str(x) for x in b])

        res = int(pow(a, int(num), mod))

        return res

        
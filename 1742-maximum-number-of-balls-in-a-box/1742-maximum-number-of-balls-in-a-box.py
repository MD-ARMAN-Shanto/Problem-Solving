class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        c = collections.Counter()
        
        def count(x):
            total = 0 
            while x > 0:
                total += x % 10
                x //= 10
            return total 
        for x in range(lowLimit, highLimit+1):
            c[count(x)] += 1
            
        return max(c.values())
        
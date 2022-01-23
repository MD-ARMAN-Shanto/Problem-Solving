class Solution:
    
    def __init__(self):
        
        self.tribase = dict()
        
        self.tribase[0] = 0
        self.tribase[1] = 1
        self.tribase[2] = 1
    
    def tribonacci(self, n: int) -> int:
        
        if n in self.tribase:
            return self.tribase[n]
        else:
            self.tribase[n] = self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
            return self.tribase[n]

        
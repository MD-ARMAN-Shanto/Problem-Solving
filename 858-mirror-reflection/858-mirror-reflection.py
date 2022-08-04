class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        
        l = math.lcm(p, q)
        
        x = (l // q) % 2 # x axis
        y = (l // p) % 2  # y axis
        
        
        if x == 1 and y == 0:
            return 0
        elif x == 1 and y == 1:
            return 1
        else:
            return 2
        
        
        
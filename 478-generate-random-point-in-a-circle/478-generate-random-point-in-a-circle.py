import random
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.xc = x_center
        self.yc = y_center

    def randPoint(self) -> List[float]:
        while True:
            X=random.uniform(self.xc - self.r, self.xc + self.r) 
            Y=random.uniform(self.yc - self.r, self.yc + self.r) 
            c=X-self.xc                                           
            d=Y-self.yc                                         
            if (c**2+d**2) < self.r**2:     
                return [X,Y]
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
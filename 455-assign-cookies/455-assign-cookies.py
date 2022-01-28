class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()
        s.sort()
        
        cookie = 0
        greed = 0
        
        while(greed < len(g) and cookie < len(s)):
            if s[cookie] >= g[greed]:
                greed += 1
            cookie += 1
        return greed
            
        
        
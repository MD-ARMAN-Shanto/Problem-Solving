class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        curr = (0,0)
        seen = {curr}
        direction = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
        
        for p in path:
            
            curr = (curr[0] + direction[p][0], curr[1] + direction[p][1])
            if curr in seen:
                return True
            seen.add(curr)
            
        return False
            
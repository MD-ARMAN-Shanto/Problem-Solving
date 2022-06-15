class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        l1 = []
        l2 = []
        
        for ch in s:
            if ch == '#' and l1:
                l1.pop()
            else:
                if ch != '#':
                    l1.append(ch)
                
        for ch in t:
            if ch == '#' and l2:
                l2.pop()
            
            else:
                if ch != '#':
                    l2.append(ch)
                
        return l1 == l2
                
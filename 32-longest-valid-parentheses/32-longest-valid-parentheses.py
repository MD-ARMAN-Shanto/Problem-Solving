class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or not stack:
                stack.append(i)
            else:
                t = stack.pop()
                if s[t] == ')':
                    stack.append(t)
                    stack.append(i)
        
        right,longest=len(s), 0
        while stack:
            left=stack.pop()
            longest=max(longest, right-left-1)
            right=left
        return max(longest,right)
    
    
                
        
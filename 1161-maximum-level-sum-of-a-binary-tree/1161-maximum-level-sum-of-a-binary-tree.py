# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        max_sum = float("-inf")
        q, level, ans = deque(), 0, 0
        q.append(root)
        
        while q:
            current_sum = 0
            level += 1
            
            for _ in range(len(q)):
                node = q.popleft()
                current_sum += node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            if current_sum > max_sum:
                max_sum = current_sum
                ans = level
                
                
        return ans
        
            
        
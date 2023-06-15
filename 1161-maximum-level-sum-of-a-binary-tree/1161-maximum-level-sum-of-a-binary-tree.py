# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
#         def dfs(node, level):
#             if not node:
#                 return 0
            
#             level_sum[level] += node.val
            
#             dfs(node.left, level+1)
#             dfs(node.right, level+1)
        
#         level_sum = collections.defaultdict(int)
#         dfs(root, 1)
#         ans, maximum = 0, float("-inf")
        
#         for level, total in level_sum.items():
#             if maximum < total:
#                 ans , maximum = level, total
            
#         return ans

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
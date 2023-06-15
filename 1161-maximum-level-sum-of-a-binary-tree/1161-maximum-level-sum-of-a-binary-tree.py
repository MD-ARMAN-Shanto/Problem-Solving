# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, level):
            if not node:
                return 0
            
            level_sum[level] += node.val
            
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        
        level_sum = collections.defaultdict(int)
        dfs(root, 1)
        ans, maximum = 0, float("-inf")
        
        for level, total in level_sum.items():
            if maximum < total:
                ans , maximum = level, total
            
        return ans
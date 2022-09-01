# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def goodNodes(self, root: TreeNode) -> int:
        
        count = self.dfs(root, root.val)
        return count 
        
    def dfs(self, root, val):
        count = 0
        if root is None:
            return count
        
        if val <= root.val:
            count += 1
        
        new_max = max(val, root.val)
        
        return count + self.dfs(root.left, new_max) + self.dfs(root.right, new_max)
        
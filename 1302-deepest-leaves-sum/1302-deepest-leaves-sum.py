# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.level_sum = []
    
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.traverse(root, 0)
        return self.level_sum[-1] # last value of the array
    
    def addToArray(self, val, level):
        if level < len(self.level_sum):
            self.level_sum[level] += val
        else:
            self.level_sum.append(val)
        
    def traverse(self, root, level):
        
        self.addToArray(root.val, level)
        
        if root.left:
            self.traverse(root.left, level+1)
        if root.right:
            self.traverse(root.right, level+1)
            
    
        
        
            
        
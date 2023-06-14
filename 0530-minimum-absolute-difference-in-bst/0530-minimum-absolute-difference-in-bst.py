# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        stack = []
        
        # in-order traversal
        def traverse(root):
            if root is None:
                return 0
            
            traverse(root.left)
            stack.append(root.val)
            traverse(root.right)
            
        traverse(root)        
        diff = min( stack[i] - stack[i-1] for i in range(1, len(stack) ) ) 
            
        return diff
        
        
        
        
        
        
        
        
        
        
        
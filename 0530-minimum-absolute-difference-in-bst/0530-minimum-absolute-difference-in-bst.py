# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        stack = []
        
        def append_to_stack(root):
            if root is None:
                return 0
            
            if root.val not in stack:
                stack.append(root.val)
                
        def traverse(root):
            append_to_stack(root)
            
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
            
        traverse(root)
        stack.sort()
        
        diff = min( stack[i] - stack[i-1] for i in range(1, len(stack) ) ) 
            
        return diff
        
        
        
        
        
        
        
        
        
        
        
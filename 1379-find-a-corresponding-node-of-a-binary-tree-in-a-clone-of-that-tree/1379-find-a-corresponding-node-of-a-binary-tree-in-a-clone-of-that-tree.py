# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
          # inorder solution
#         def inorder(o, c):
#             if o:
#                 inorder(o.left, c.left)
#                 if o is target:
#                     self.ans = c
#                 inorder(o.right, c.right)
        
#         inorder(original, cloned)
#         return self.ans
        # preorder solution
    
        def preorder(node):
            if node.val == target.val:
                self.result = node
                
            if node.left != None:
                preorder(node.left)
                
            if node.right != None:
                preorder(node.right)
                
        if cloned:
            preorder(cloned)
            
        return self.result
                
                
                
                
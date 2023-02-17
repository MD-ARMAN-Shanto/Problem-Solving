class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        self.cur = None
        self.minimum = float('inf')

        def inorder(node):
            if node:
                inorder(node.left)
                if self.cur:
                    self.minimum = min(self.minimum, node.val - self.cur.val)
                self.cur = node
                inorder(node.right)

        inorder(root)
        return self.minimum
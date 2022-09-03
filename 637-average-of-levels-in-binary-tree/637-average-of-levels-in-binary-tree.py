# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        lvlcnt = defaultdict(int)
        lvlsum = defaultdict(int)

        def dfs(node=root, level=0):
            if not node: return
            lvlcnt[level] += 1
            lvlsum[level] += node.val
            dfs(node.left, level+1)
            dfs(node.right, level+1)

        dfs()
        return [lvlsum[i] / lvlcnt[i] for i in range(len(lvlcnt))]
        
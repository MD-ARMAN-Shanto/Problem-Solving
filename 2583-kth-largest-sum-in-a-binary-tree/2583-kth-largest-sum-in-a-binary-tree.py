# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        def dfs(node, level):
            if not node:
                return 0
            
            level_sum[level] += node.val
            
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        
        
        level_sum = collections.defaultdict(int)
        dfs(root, 1)
        sum_array = []
        
        for level, total in level_sum.items():
            # if len(sum_array) > 0:
            #     max_val = max(sum_array)
                
            sum_array.append(total)
            
        
        # tim sort
#         for i in range(len(sum_array)):
#             min_index = i
#             for j in range(i+1, len(sum_array)):
#                 if sum_array[min_index] < sum_array[j]:
#                     min_index = j
                    
#             sum_array[i], sum_array[min_index] = sum_array[min_index], sum_array[i]

        res = sorted(sum_array, reverse=True)
                            
        if k > len(res):
            return -1
        
        return res[k-1]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
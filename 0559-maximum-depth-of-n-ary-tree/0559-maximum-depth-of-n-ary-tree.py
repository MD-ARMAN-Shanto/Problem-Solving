"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        
        nodesTocheck = [(root, 1)]
        maxDepth = 0
        
        while nodesTocheck:
            current_node, depth = nodesTocheck.pop()
            
            if current_node.children:
                for node in current_node.children:
                    nodesTocheck.append((node, depth+1))
                    
            if depth > maxDepth:
                maxDepth = depth
                
        return maxDepth
                
                
            
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        s = set()
        tmp = head
        
        while tmp:
            
            if tmp in s:
                return True
            
            s.add(tmp)
            tmp = tmp.next
            
        return False
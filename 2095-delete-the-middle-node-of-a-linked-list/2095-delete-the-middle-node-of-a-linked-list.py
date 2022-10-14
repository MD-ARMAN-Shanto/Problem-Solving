# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head.next == None:
            return None
        
        count = 0
        p1 = p2 = head
        
        while p1:
            count += 1
            p1 = p1.next
            
        middle_index = count // 2
        
        for _ in range(middle_index - 1):
            p2 = p2.next
            
        
        p2.next = p2.next.next
        return head
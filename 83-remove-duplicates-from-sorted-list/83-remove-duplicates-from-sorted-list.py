# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = head
        
        if temp is None:
            return
        
        while temp.next != None:
            if temp.next.val == temp.val:
                new = temp.next.next
                temp.next = None
                temp.next = new
            else:
                temp = temp.next
                
        return head
                
                
                
                
                
                
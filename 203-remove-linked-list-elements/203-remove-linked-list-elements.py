# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        current_node = head
        previous_node = None
        
        while current_node:
            # check node val == val
            if current_node.val == val:
                # check it's head value or not
                if current_node == head:
                    head = head.next
                    current_node = head
                # if referrence node
                else:
                    previous_node.next = current_node.next
                    current_node = previous_node
                    
            else:
                previous_node = current_node
                current_node = previous_node.next
                
        return head
    
    
    
    
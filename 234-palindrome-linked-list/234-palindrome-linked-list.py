# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        
        # find the middle of linked list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse a list
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            
        # check palindrome or not
        left, right = head, prev
        
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        return True
        
        
    
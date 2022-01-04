# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        nHead, h1, h2 = None, l1, l2
        run = None
        c = 0
        while h1 and h2:
            s = h1.val + h2.val + c
            c = s // 10
            s = s % 10
            temp = ListNode(s)
            
            if not nHead:
                nHead = temp
                run = temp
            else:
                run.next = temp # assign head next address to next val
                run = run.next  # assign new run address 
            h1 = h1.next
            h2 = h2.next
            
        # if h1 has more nodes than h2
        while h1:
            s = h1.val + c
            c = s // 10
            s = s % 10
            run.next = ListNode(s)
            run = run.next
            h1 = h1.next
            
        #if h2 has more nodes than h1
        while h2:
            s = h2.val + c
            c = s // 10
            s = s % 10
            run.next = ListNode(s)
            run = run.next
            h2 = h2.next
        
        # no nodes left but we have the only carry value 1 exists
        if c != 0:
            run.next = ListNode(c)
            run = run.next
        
        return nHead
            
        
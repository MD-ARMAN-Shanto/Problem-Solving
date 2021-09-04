"""
Approach: linearSearch
Status: Accepted
131 / 131 test cases passed.
Runtime: 96 ms
Memory Usage: 15.6 MB
Problem link: https://leetcode.com/problems/reverse-linked-list/
Time complexity: O(n)
space complexity: O(1)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev = None

        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp

        return prev

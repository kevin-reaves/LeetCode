#!/usr/bin/python

"""
Given a sorted linked list, delete all duplicates such that each element
appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

    def printList(self, head):
        current = head
        while current:
            print(current.val)
            current = current.next

head = ListNode(100)
node1 = ListNode(101)
node2 = ListNode(101)
node3 = ListNode(102)
node4 = ListNode(103)

head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4

solution = Solution()
answer = solution.deleteDuplicates(head)
solution.printList(answer)
"""
@File    : 141.环形链表.py
@Time    : 2019-09-29 22:30
@Author  : Wade
@Software: PyCharm
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        fast=head.next
        slow=head
        while slow!=fast:
            if fast and fast.next:
                fast=fast.next.next
                slow=slow.next
            else:
                return False
        return True



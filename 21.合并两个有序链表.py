#将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        if l1.val < l2.val:
            head = l1
        else:
            head = l2
            temp = l1
            l1 = l2
            l2 = temp

        while l1 and l2:
            if l1.next == None:
                l1.next = l2
                return head
            if l1.val < l2.val and l1.next.val < l2.val:
                l1 = l1.next
                continue
            if l1.val <= l2.val and l1.next.val >= l2.val:
                p = l2
                l2 = l2.next
                p.next = l1.next
                l1.next = p
        return head
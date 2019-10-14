#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        if head == None or head.next == None:
            return head
        p = head
        q = p.next
        result=ListNode(0)
        result.next=q
        pre=result
        while p != None and q != None:
            p.next = q.next
            q.next = p
            pre.next=q

            pre=p
            p=p.next
            q=p.next if p!=None else None
        return result.next

# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#  
#
# 示例:
#
# 给定 1->2->3->4, 你应该返回 2->1->4->3.


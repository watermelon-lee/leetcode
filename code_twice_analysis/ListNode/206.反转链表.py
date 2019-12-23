"""
@File    : 206.反转链表.py
@Time    : 2019-12-23 16:04
@Author  : LEE
@Software: PyCharm
@Email: leehaoran@pku.edu.cn
"""

# 类型 链表

# 思路

# 迭代法
# 首先长度为0或者长度为1直接返回
# 否则，遍历找到最后一个节点，将其拆出作为反转之后链表的头节点
# 之后对原始链表从头开始，对每个节点使用头插法插入反转链表中


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        # 空链表
        if not head:
            return None
        # 单个节点
        if not head.next:
            return head
        # 就地反转，不使用而外空间

        # 拆下最后一个节点作为反转链表的头节点
        p=head
        while p.next!=None and p.next.next!=None:
            p=p.next
        h=p.next
        p.next=None


        p=head
        r=p.next
        while p!=None:
            p.next=h.next
            h.next=p
            p=r
            if p:
                r=p.next
        return h


h=ListNode(1)
h.next=ListNode(2)
S=Solution()
head=S.reverseList(h)
while head:
    print(head.val)
    head=head.next
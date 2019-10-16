"""
@File    : 148.排序链表.py
@Time    : 2019-10-15 23:12
@Author  : 李浩然
@Software: PyCharm
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        # fing mid
        # 使用双指针，fast走到尾部，slow在中间
        slow,fast=head,head.next
        while fast and fast.next:
            fast,slow=fast.next.next,slow.next
        # cut
        # 从slow右边切断
        mid,slow.next=slow.next,None

        left,right=self.sortList(head),self.sortList(mid)


        #生成一个新的节点来合并
        h=res=ListNode(0)

        while left and right:
            if left.val<right.val:
                h.next=left
                left=left.next
            else:
                h.next=right
                right=right.next
            h=h.next
        # left , right有可能还有元素
        h.next=left if left else right

        return res.next
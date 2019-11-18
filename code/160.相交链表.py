"""
@File    : 160.相交链表.py
@Time    : 2019-11-18 16:26
@Author  : 李浩然
@Software: PyCharm
@Email: 1901210423@pku.edu.cn
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len1=0
        len2=0

        node1=headA
        node2=headB

        while node1:
            len1+=1
            node1=node1.next
        while node2:
            len2+=1
            node2=node2.next
        print(len1,len2)


        node_long=None
        node_short=None

        if len2>len1:
            node_short=headA
            node_long=headB
            temp=len1
            len1=len2
            len2=temp
        else:
            node_short=headB
            node_long=headA

        while len2<len1:
            len1-=1
            node_long=node_long.next

        while node_long:
            if node_short==node_long:
                return node_long
            else:
                print(node_long.val)
                node_long=node_long.next
                print(node_long.val)
                print(node_short.val)
                node_short=node_short.next
                print(node_short.val)

        return None



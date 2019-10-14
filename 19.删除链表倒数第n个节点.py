
#给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p=head
        q=head
        count=1
        while n>0 and p.next!=None :
            p=p.next
            count +=1
            n=n-1
        while p.next!=None:
            q=q.next
            count+=1
            p=p.next
        if count==1:
            return head.next
        if q==head and n==1:
            return head.next
        p=q.next
        q.next=p.next
        return head
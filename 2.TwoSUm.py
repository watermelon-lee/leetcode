#给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

#如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

#您可以假设除了数字 0 之外，这两个数都不会以 0 开头。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        re = ListNode(0)
        r=re
        flag=0
        while l1 or l2:
            if l1:
                x=l1.val
            else:
                x=0
            if l2:
                y=l2.val
            else:
                y=0
            sum=flag+x+y
            flag=sum//10 #取整除法//  小数/
            r.next=ListNode(sum%10)
            r=r.next
            if l1!=None:
                l1=l1.next
            if l2!=None:
                l2=l2.next
        if flag:
            r.next=ListNode(flag)
        return re.next



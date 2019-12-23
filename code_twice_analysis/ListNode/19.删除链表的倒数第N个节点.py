"""
@File    : 19.删除链表的倒数第N个节点.py
@Time    : 2019-12-16 11:20
@Author  : 李浩然
@Software: PyCharm
@Email: leehaoran@pku.edu.cn
"""

# 类型 链表
# 技巧 双指针

# 思路
# 要实现一遍遍历，我们需要找到倒数第N个节点的前一个节点
# 我们使用双指针，首指针在头节点，尾指针在头节点N个节点之后
# 两者同步向后遍历，尾指针到达最后一个节点，首指针即在倒数N+1个节点

# 唯一不同的情况就是删除的是head节点
# 我们使用count记录链表长度，count=n时，删除第一个，返回head.next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        front,tail=head,head
        count=1 # 用来记录长度
        while n>=count and tail.next:
            tail=tail.next
            count+=1
        while tail.next:
            tail=tail.next
            count+=1
            front=front.next
        if count==n:
            return head.next
        front.next=front.next.next
        return head

a=ListNode(1)
b=ListNode(2)
a.next=b

S=Solution()

head=S.removeNthFromEnd(a,2)
while head:
    print(head.val)
    head=head.next
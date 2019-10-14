# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        #
        # node=set()
        # while head:
        #     if head not in node:
        #         node.add(head)
        #         head=head.next
        #     if head in node:
        #         return head
        #
        # return None

        slow=head
        fast=head.next
        count,step=0,0
        while count!=2:
            print(count)
            if fast and fast.next:
                fast=fast.next.next
                slow=slow.next
                if count==1:
                    step+=1
            else:
                return None
            if fast==slow:
                count+=1
        print(count,step)
        start1,start2=head,head
        while step>0:
            step-=1
            start1=start1.next
        while start1!=start2:
            start1=start1.next
            start2=start2.next

        return start1
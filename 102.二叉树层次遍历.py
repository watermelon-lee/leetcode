"""
@File    : 102.二叉树层次遍历.py
@Time    : 2019-10-08 18:44
@Author  : Wade
@Software: PyCharm
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        now,end,next_end=0,1,1
        queue=[root]
        ans=[]
        while len(queue)>0:
            temp=[]
            while now<end:
                temp.append(queue[0].val)
                if queue[0].left:
                    queue.append(queue[0].left)
                    next_end+=1
                if queue[0].right:
                    queue.append(queue[0].right)
                    next_end+=1
                queue.remove(queue[0])
                now+=1
            ans.append(temp)
            end=next_end
        return ans







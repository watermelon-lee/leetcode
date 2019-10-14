"""
@File    : 104.二叉树的最大深度.py
@Time    : 2019-10-08 19:12
@Author  : Wade
@Software: PyCharm
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.findLevel(root)


    def findLevel(self,node):
        if not node:
            return 0
        return max(self.findLevel(node.left)+1,self.findLevel(node.right)+1)
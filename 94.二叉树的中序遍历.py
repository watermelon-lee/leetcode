"""
@File    : 94.二叉树的中序遍历.py
@Time    : 2019-09-24 13:54
@Author  : Wade
@Software: PyCharm
"""



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
class Solution:

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        # def order(root):
        #     if not root:
        #         return
        #     order(root.left)
        #     ans.append(root.val)
        #     order(root.right)
        # order(root)
        # return ans
        stack=[]
        now=root
        while len(stack)>0 or now:
            if now:
                stack.append(now)
                now = now.left
            else:
                now=stack.pop()
                ans.append(now.val)
                now=now.right
        return ans




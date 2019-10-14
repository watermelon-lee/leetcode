"""
@File    : 101.对称二叉树.py
@Time    : 2019-09-27 15:35
@Author  : Wade
@Software: PyCharm
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


### 递归
# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         ans1=[]
#         ans2=[]
#         self.orderleft(root,ans1)
#         self.orderright(root,ans2)
#         return ans1==ans2
#
#
#
#     def orderleft(self,root,ans):
#         if not root:
#             ans.append(0)
#             return
#         ans.append(root.val)
#         self.orderleft(root.left,ans)
#         self.orderleft(root.right,ans)
#
#     def orderright(self,root,ans):
#         if not root:
#             ans.append(0)
#             return
#         ans.append(root.val)
#         self.orderright(root.right,ans)
#         self.orderright(root.left,ans)

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue=[root,root]
        while queue:
            one=queue.pop(0)
            two=queue.pop(0)
            if not one and not two:
                continue
            if not one or not two:
                return False
            if one.val!=two.val:
                return False
            queue.append(one.left)
            queue.append(two.right)
            queue.append(one.right)
            queue.append(two.left)
        return True


"""
@File    : 98.验证二叉搜索树.py
@Time    : 2019-12-18 20:20
@Author  : 李浩然
@Software: PyCharm
@Email: leehaoran@pku.edu.cn
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    pre=TreeNode(-pow(2,32))
    def isValidBST(self, root: TreeNode) -> bool:


        # 错误的想法
        # 不能保证右子树每一个节点都大于root，也不能保证左子树所有节点大于root
        # if not root:
        #     return True
        #
        # if root.right and root.left:
        #     if root.left.val>=root.val or root.right.val<=root.val:
        #         return False
        #     else:
        #         return self.isValidBST(root.left) and self.isValidBST(root.right)
        # elif root.left:
        #     if root.left.val>=root.val:
        #         return False
        #     else:
        #         return self.isValidBST(root.left)
        # elif root.right:
        #     if root.right.val <= root.val:
        #         return False
        #     else:
        #         return self.isValidBST(root.right)
        # else:
        #     return True





a=TreeNode(5)
b=TreeNode(2)
c=TreeNode(6)
d=TreeNode(15)
e=TreeNode(10)
f=TreeNode(20)

e.left=a
e.right=d
d.left=c
d.right=f


S=Solution()

print(S.isValidBST(e))
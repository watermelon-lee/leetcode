"""
@File    : 114.二叉树展开为链表.py
@Time    : 2019-11-29 15:07
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
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        while root!=None:
            if root.left==None:
                root=root.right
            else:
                # 找到左子树最右边节点
                pre=root.left
                while pre.right!=None:
                    pre=pre.right
                pre.right=root.right
                root.right=root.left
                root.left=None

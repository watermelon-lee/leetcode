"""
@File    : 105.从前序与中序遍历构造二叉树.py
@Time    : 2019-11-29 14:43
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




from typing import List

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        if not inorder:
            return None

        root_value=preorder[0]
        root=TreeNode(root_value)

        root_index_inorder=inorder.index(root_value)
        root.left=self.buildTree(preorder[1:root_index_inorder+1],inorder[:root_index_inorder])
        root.right=self.buildTree(preorder[root_index_inorder+1:],inorder[root_index_inorder+1:])

        return root



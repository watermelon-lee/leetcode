"""
@File    : 94.二叉树的中序遍历.py
@Time    : 2019-12-17 12:54
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


# 类型 树
# 技巧 栈

# 思路
# 树的三种遍历递归方式都很简单，使用迭代实现
# 我们使用栈保存我们遍历的节点
# 前序遍历是每走到一个就要保存，先向左，后向右

# 1 我们遍历到一个节点，就将其加入栈,然后向其左子树遍历
# 2 若当前节点不为空，继续向左遍历
# 3 若当前节点为空，元素出栈，并且保存结果，出栈元素即为这个空节点的父节点，然后向右遍历
# 回到 1
# 重复上述步骤，直到当前节点为空，而且也没有父节点（栈为空）

# 代码与前序遍历一致，只是在保存结果的地方有所不同

from typing import List
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []

        # def in_order(root):
        #     if not root:
        #         return
        #     in_order(root.left)
        #     ans.append(root.val)
        #     in_order(root.right)
        #
        # in_order(root)

        stack=[]
        now=root
        while stack or now:
            if now:
                stack.append(now)
                now=now.left
            else:
                now=stack.pop()
                ans.append(now.val)
                now=now.right
        return ans

"""
@File    : 144.二叉树的前序遍历.py
@Time    : 2019-12-17 12:45
@Author  : 李浩然
@Software: PyCharm
@Email: leehaoran@pku.edu.cn
"""

# 类型 树
# 技巧 栈

# 思路
# 树的三种遍历递归方式都很简单，使用迭代实现
# 我们使用栈保存我们遍历的节点
# 前序遍历是每走到一个就要保存，先向左，后向右

# 1 我们遍历到一个节点，就将其加入栈，并且保存结果，然后向其左子树遍历
# 2 若当前节点不为空，继续向左遍历
# 3 若当前节点为空，元素出栈，即为这个空节点的父节点，然后向右遍历
# 回到 1
# 重复上述步骤，直到当前节点为空，而且也没有父节点（栈为空）



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans=[]

        # def prior_order(root):
        #     if not root:
        #         return
        #     ans.append(root.val)
        #     prior_order(root.left)
        #     prior_order(root.right)
        #
        # prior_order(root)



        stack=[]
        now=root
        while stack or now:
            if now:
                stack.append(now)
                ans.append(now.val)
                now=now.left
            else:
                now=stack.pop()
                now=now.right
        return ans

a=TreeNode(1)
b=TreeNode(2)
c=TreeNode(3)
a.right=b
b.left=c

S=Solution()

print(S.preorderTraversal(a))
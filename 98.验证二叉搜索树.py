"""
@File    : 98.验证二叉搜索树.py
@Time    : 2019-09-27 15:10
@Author  : Wade
@Software: PyCharm
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack=[]
        now = root
        ans=[]
        while len(stack) > 0 or now:
            if now:
                stack.append(now)
                now = now.left
            else:
                now = stack.pop()
                ans.append(now.val)
                now = now.right
        for i in range(0,len(ans)-1):
            if ans[i]>=ans[i+1]:
                return False
        return True




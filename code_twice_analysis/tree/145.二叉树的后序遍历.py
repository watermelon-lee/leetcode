"""
@File    : 145.二叉树的后序遍历.py
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
# 技巧 栈/双指针

# 依旧是与前后序写法类似，但是我们需要额外加入一个指针pre，表示上一个访问过的节点
# 当当前节点的右子树是pre时，就代表该节点右子树以及访问完毕，就可以访问该节点了


from typing import List

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        ans=[]

        # def post_order(root):
        #     if not root:
        #         return
        #     post_order(root.left)
        #     post_order(root.right)
        #     ans.append(root.val)
        #
        # post_order(root)

        stack=[]
        now=root
        pre=None
        while now or stack:
            if now:
                stack.append(now)
                now=now.left
            else:
                now=stack[-1] # 先不出栈，而是观察其右节点是否被访问过
                if not now.right or now.right==pre: # 若右子树也为空或者右子树已经被访问，则可输出该节点
                    ans.append(now.val)
                    stack.pop()
                    pre=now
                    now=None
                else:
                    now=now.right


        return ans

# 更巧妙的解法
# 后序遍历是左右中
# 前序遍历若优先向右而不是向左，那就是 中右左，其逆序是左右中，与后序遍历一致
#
class Solution2:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        ans=[]

        stack=[]
        now=root

        while stack or now:
            if now:
                stack.append(now)
                ans.append(now.val)
                now=now.right
            else:
                now=stack.pop()
                now=now.left
        return ans[::-1] #返回逆序

a=TreeNode(1)
b=TreeNode(2)
c=TreeNode(3)
a.right=b
b.left=c

S=Solution2()

print(S.postorderTraversal(a))
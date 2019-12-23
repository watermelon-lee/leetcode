"""
@File    : 100.相同的树.py
@Time    : 2019-12-18 13:22
@Author  : 李浩然
@Software: PyCharm
@Email: leehaoran@pku.edu.cn
"""


# 类型 树
# 技巧 回溯/队列

# 思路

# 回溯
# 我们同时从两棵树的根节点p，q开始遍历。
# 若p，q相等则递归的对p，q的左儿子与右儿子进行比较
# 若全部相等，则最后返回true，否则返回false

# 队列
# 使用迭代的方式进行比较
# 我们将p，q依次入队，进行比较，若相等，则在将p，q的左右儿子均加入
# 然后每次取出对头两个元素进行比较，直到最后队列为空
# 若全部相等则返回True，若有一个不想等则直接返回false

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        # # 递归
        # if not p and not q:# q,p都是空，则相同
        #     return True
        # elif not p or not q: # p，q有一个空，不同（因为上一个条件已经滤去了p，q均为空了）
        #     return False
        # elif p.val!=q.val:
        #     return False
        # else:
        #     return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)




        # 迭代
        queue=[(p,q)]

        while queue:
            p,q=queue.pop(0)

            if not p and not q:# q,p都是空，则相同
                pass
            elif not p or not q: # p，q有一个空，不同（因为上一个条件已经滤去了p，q均为空了）
                return False
            elif p.val!=q.val:
                return False
            else:
                queue.append((p.left,q.left))
                queue.append((p.right,q.right))
        return True


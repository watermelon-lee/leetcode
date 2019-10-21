"""
@File    : 96.不同的二叉搜索树.py
@Time    : 2019-10-21 09:43
@Author  : 李浩然
@Software: PyCharm
"""


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        G=[0 for i in range(n+1)]
        G[0],G[1]=1,1
        for i in range(2,n+1):
            for j in range(1,n+1):
                G[i]+=G[j-1]*G[i-j]
        return G[n]

s=Solution()
print(s.numTrees(3))
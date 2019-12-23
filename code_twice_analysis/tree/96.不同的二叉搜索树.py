"""
@File    : 96.不同的二叉搜索树.py
@Time    : 2019-12-18 13:45
@Author  : 李浩然
@Software: PyCharm
@Email: leehaoran@pku.edu.cn
"""


# 类型 树
# 技巧 动态规划

# 思路
# 使用Gn表示n个节点所能组成的二叉搜索树
# 在n个节点中，以1为根节点，则左子树为空树，即为G0，右子树为2-n个节点组成的搜索树，即为Gn-1
# 然后以2为根节点，左边为1组成搜索树，即为G1，右边为3-n组成的搜索树，即为Gn-3
# 而左子树有Gleft中可能，右子树有Grihgt种可能时，总共有Gleft*Gright种可能
# 所以可以得到递推式：Gn=(G0*Gn-1 + G1*Gn-2 + ...+ Gn-2*G1 + Gn-1*G0)


class Solution:
    def numTrees(self, n: int) -> int:
        G=[0 for _ in range(n+1)]

        G[0]=1
        G[1]=1
        for i in range(2,n+1):
            for j in range(0,i):
                G[i]+=G[j]*G[i-1-j]
        return G[n]

S=Solution()

print(S.numTrees(3))
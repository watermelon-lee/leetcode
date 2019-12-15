"""
@File    : 62.不同路径.py
@Time    : 2019-12-15 10:29
@Author  : 李浩然
@Software: PyCharm
@Email: leehaoran@pku.edu.cn
"""


# 动态规划

# 思路
# 使用dp【i】【j】表示从i到j的路径有多少条
# 初始化第一排，第一列都只有一种走法
# dp[i][j] = dp[i - 1][j] + dp[i][j - 1]



class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0 for _ in range(m)] for _ in range(n)]
        # 初始化
        for i in range(n):
            dp[i][0]=1
        for i in range(m):
            dp[0][i]=1
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]

        return dp[n-1][m-1]

s=Solution()
print(s.uniquePaths(3,2))
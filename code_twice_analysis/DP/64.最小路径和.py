"""
@File    : 64.最小路径和.py
@Time    : 2019-12-15 20:44
@Author  : 李浩然
@Software: PyCharm
@Email: leehaoran@pku.edu.cn
"""

from typing import List



# 动态规划

# 思路
# 使用dp【i】【j】表示从i到j的路径有多少条
# 初始化第一排，第一列都只有一种走法 dp[i][0]=dp[i-1][0]+grid[i][0]
# 之后的遍历
# 只有从上，左两个方向走到当前位置，我们选取上，左两个方向中较小的路径和，然后更新当前点
# dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid) #行
        m=len(grid[0]) #列

        dp=[[0 for _ in range(m)] for _ in range(n)]

        dp[0][0]=grid[0][0]
        for i in range(1,n):
            dp[i][0]=dp[i-1][0]+grid[i][0]
        for i in range(1,m):
            dp[0][i]=dp[0][i-1]+grid[0][i]

        for i in range(1,n):
            for j in range(1,m):
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[n-1][m-1]


s=Solution()
grid=[[1,2,5],[3,2,1]]
print(s.minPathSum(grid))
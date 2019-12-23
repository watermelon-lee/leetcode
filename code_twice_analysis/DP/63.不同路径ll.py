"""
@File    : 63.不同路径ll.py
@Time    : 2019-12-15 20:11
@Author  : 李浩然
@Software: PyCharm
@Email: leehaoran@pku.edu.cn
"""


# 动态规划

# 思路
# 使用dp【i】【j】表示从i到j的路径有多少条
# 初始化第一排，第一列
# 若有障碍物，dp【i】【j】=0
# 没有障碍物，则到这个位置等于到前一个位置的走法 dp[i][0]=dp[i-1][0]
# 从1，1处开始遍历
# 若无障碍物
# dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
# 若有障碍物
#  dp[i][j】=0



from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n=len(obstacleGrid) #行
        m=len(obstacleGrid[0]) # 列
        dp=[[0 for _ in range(m)] for _ in range(n)]
        if obstacleGrid[0][0]==0:
            dp[0][0]=1
        else:
            dp[0][0]=0
        # 初始化
        for i in range(1,n):
            if obstacleGrid[i][0]==0:
                dp[i][0]=dp[i-1][0]
            else:
                dp[i][0]=0
        for i in range(1,m):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = dp[0][i-1]
            else:
                dp[0][i] = 0

        for i in range(1,n):
            for j in range(1,m):
                if obstacleGrid[i][j]==0:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
                else:
                    dp[i][j]=0

        return dp[n-1][m-1]

S=Solution()
o=[
  [1]
]
print(S.uniquePathsWithObstacles(o))
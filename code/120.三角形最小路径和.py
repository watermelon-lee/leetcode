"""
@File    : 120.三角形最小路径和.py
@Time    : 2019-10-21 08:42
@Author  : 李浩然
@Software: PyCharm
"""

from typing import List
import math


#采用自底向上更加方便编码

# dp[i][j]=min(dp[i+1][j],dp[i+1][j+1])+triangle[i][j]

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        m = len(triangle)  # 行
        n = len(triangle[m-1])  # 最后一行列数

        if m == 0 and n == 0:
            return 0

        dp = []
        for i in range(len(triangle)):
            dp.append([0 for i in range(i+1)])
        dp[0][0] = triangle[0][0]


        for i in range(1, m):
            for j in range(len(triangle[i])):
                if j - 1 >= 0 and j < len(triangle[i-1]):
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
                elif j - 1 >= 0:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                else:
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
        maxPath = 10000000
        for j in range(n):
            maxPath = dp[m-1][j] if dp[m-1][j] < maxPath else maxPath
        return maxPath


s=Solution()
tr=[
     [-2],
    [-3,-4]
]
print(s.minimumTotal(tr))



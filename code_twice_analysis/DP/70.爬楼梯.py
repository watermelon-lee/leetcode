"""
@File    : 70.爬楼梯.py
@Time    : 2019-12-15 21:00
@Author  : 李浩然
@Software: PyCharm
@Email: leehaoran@pku.edu.cn
"""

# 类型 动态规划

# 思路
# 当前位置 可以从前一阶到达，也可从前两阶到达
# dp[i]=dp[i-1]+dp[i-2]

class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        dp=[0 for _ in range(n)]
        dp[0]=1

        dp[1]=2
        for i in range(2,n):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n-1]

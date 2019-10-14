"""
@File    : 121.买股票的最佳时机.py
@Time    : 2019-10-14 11:12
@Author  : 李浩然
@Software: PyCharm
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices)==1:
            return 0
        profits=[prices[i+1]-prices[i] for i in range(0,len(prices)-1)]
        dp=[0 for _ in range(len(profits))]
        dp[0] = max(0, profits[0])
        ans=dp[0]
        for i in range(1,len(prices)-1):
            dp[i]=max(0,dp[i-1]+profits[i])
            ans=max(ans,dp[i])
        return ans


s=Solution()
prices=[1,2]
print(s.maxProfit(prices))
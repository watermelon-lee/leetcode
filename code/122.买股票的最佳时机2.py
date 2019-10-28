"""
@File    : 122.买股票的最佳时机2.py
@Time    : 2019-10-28 08:43
@Author  : 李浩然
@Software: PyCharm
@Email: 1901210423@pku.edu.cn
"""

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        price_buy=0
        price_sold=0
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                price_buy=prices[i]
                price_sold=prices[i+1]
                profit+=(price_sold-price_buy)
        return profit

s=Solution()
prices=[7,1,5,3,6,4]
print(s.maxProfit(prices))
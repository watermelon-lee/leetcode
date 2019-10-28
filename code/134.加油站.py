"""
@File    : 134.加油站.py
@Time    : 2019-10-28 09:06
@Author  : 李浩然
@Software: PyCharm
@Email: 1901210423@pku.edu.cn
"""


from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff=0
        for i in range(len(cost)):
            diff+=gas[i]-cost[i]
        if diff<0:
            return -1
        else:
            curr_gas=0
            start=0
            for i in range(len(cost)):
                curr_gas+=gas[i]-cost[i]
                if curr_gas<0:
                    curr_gas=0
                    start=i+1
        return start


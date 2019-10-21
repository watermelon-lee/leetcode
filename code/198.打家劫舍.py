"""
@File    : 198.打家劫舍.py
@Time    : 2019-10-21 09:58
@Author  : 李浩然
@Software: PyCharm
"""
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp=[0 for i in range(len(nums))]
        dp[0]=nums[0]

        for i in range(1,len(nums)):
            if i==1:
                dp[i]=max(nums[1],dp[i-1])
            else:
                dp[i]=max(dp[i-2]+nums[i],dp[i-1])
        return max(dp[len(nums)-1],dp[len(nums)-2])

s=Solution()
nums=[2,1,1,2]
print(s.rob(nums))
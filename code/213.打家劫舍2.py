"""
@File    : 213.打家劫舍2.py
@Time    : 2019-10-21 10:44
@Author  : 李浩然
@Software: PyCharm
"""

from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        dp1=[0 for _ in range(1,len(nums)+1)]
        dp2=[0 for _ in range(1,len(nums)+1)]
        dp1[0]=nums[0]
        dp2[1]=nums[1]
        for i in range(1,len(nums)-1):
            if i==1:
                dp1[i]=max(dp1[0],nums[1])
            else:
                dp1[i]=max(dp1[i-1],dp1[i-2]+nums[i])
        for i in range(2,len(nums)):
            if i==2:
                dp2[i]=max(dp2[i-1],nums[2])
            else:
                dp2[i]=max(dp2[i-1],dp2[i-2]+nums[i])
        return max(dp1[len(nums)-2],dp2[len(nums)-1])

s=Solution()
print(s.rob([1,2]))
"""
@File    : 53.最大子序和.py
@Time    : 2019-12-13 11:04
@Author  : 李浩然
@Software: PyCharm
@Email: leehaoran@pku.edu.cn
"""


# 类型 动态规划

# 思路
# 从第一个数开始，dp【i】代表以第i个元素结尾的最大和
# dp【i】=max（dp【i-1】+nums【i】，nums【i】）


from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=nums[0]
        result=dp
        for i in range(1,len(nums)):
            dp=max(dp+nums[i],nums[i]) #以i结尾的最大和
            result=max(result,dp)
        return result

S=Solution()
nums=[-2,1,-3,4,-1,2,1,-5,4]
print(S.maxSubArray(nums))
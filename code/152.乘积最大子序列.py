"""
@File    : 152.乘积最大子序列.py
@Time    : 2019-11-18 15:37
@Author  : 李浩然
@Software: PyCharm
@Email: 1901210423@pku.edu.cn
"""

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxv=nums[0]
        minv=nums[0]
        ans=maxv
        for i in range(1,len(nums)):
            if nums[i]<0:
                # 负数交换两个值
                temp=maxv
                maxv=minv
                minv=temp
            maxv=max(nums[i],maxv*nums[i])
            minv=min(nums[i],minv*nums[i])

            #保存出现过的最大结果
            ans=max(maxv,ans)

        return ans

s=Solution()
nums=[-2]
print(s.maxProduct(nums))
"""
@File    : 136.只出现一次的数字.py
@Time    : 2019-09-23 20:28
@Author  : Wade
@Software: PyCharm
"""

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic={}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]]=1
            else:
                dic[nums[i]]+=1
        for key in dic:
            if dic[key]==1:
                return key

    # 数学方法：2∗(a+b+c)−(a+a+b+b+c)=c
    # 2 * sum(set(nums)) - sum(nums)

    # 位运算
    # 如果我们对 0 和二进制位做 XOR 运算，得到的仍然是这个二进制位
    # 如果我们对相同的二进制位做 XOR 运算，返回的结果是 0
    # XOR 满足交换律和结合律
    #         a = 0
    #         for i in nums:
    #             a ^= i
    #         return a


s=Solution()
print(s.singleNumber([1,2,3,1,2,3,4]))
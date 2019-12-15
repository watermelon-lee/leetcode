"""
@File    : 26.删除排序数组中重复项.py
@Time    : 2019-12-10 12:40
@Author  : 李浩然
@Software: PyCharm
@Email: leehaoran@pku.edu.cn
"""

# 类型 数组
# 技巧 双指针

# 两个指针初始均指向第二个元素
# count用于计算当前不同元素，并遇到不同元素修改时数组count位置的元素，然后后移一位
# i指针遍历数组，当i指针元素与前一个元素不同，就可以更新count指针位置处值

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[count]=nums[i]
                count+=1
        return count


nums = [0,0,1,1,1,2,2,3,3,4],
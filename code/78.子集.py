"""
@File    : 78.子集.py
@Time    : 2019-09-23 08:38
@Author  : Wade
@Software: PyCharm
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        if size == 0:
            return []

        res = []
        self.__dfs(nums, 0, [], res)
        return res

    def __dfs(self, nums, start, path, res):
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            # 因为 nums 不包含重复元素，并且每一个元素只能使用一次
            # 所以下一次搜索从 i + 1 开始
            self.__dfs(nums, i + 1, path, res)
            path.pop()
"""
@File    : 11.盛水最多的容器.py
@Time    : 2019-12-09 16:16
@Author  : 李浩然
@Software: PyCharm
@Email: leehaoran@pku.edu.cn
"""


# 类型 数组
# 技巧 双指针

# 思路
# 使用双指针从两头遍历，由于面积被较短的一端限制
# 为了获得更大的面积，我们舍弃较小的一端，虽然我们矩形长度减少，但是我们可能获得更高的高度
# 每一次遍历获得最大值就保留，最后得到最大的面积。

from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right=0,len(height)-1

        max_water=-1
        while left<right:
            tmp_max=(right-left)*min(height[left],height[right])
            if tmp_max>max_water:
                max_water=tmp_max
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return max_water



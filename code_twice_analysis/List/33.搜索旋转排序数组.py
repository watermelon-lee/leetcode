"""
@File    : 33.搜索旋转排序数组.py
@Time    : 2019-12-11 20:26
@Author  : 李浩然
@Software: PyCharm
@Email: leehaoran@pku.edu.cn
"""

# 类型 数组
# 技巧 二分，双指针

# 思路
# 若数组进行了旋转，则变成了两段有序的数组。我们在头尾设置指针l，r。
# 可知nums【l】为第一段元素最小值，nums【r】为第二段最大值
# 我们查找两个数组中间值nums【mid】。

# 当nums【mid】=target 直接返回
# 否则，我们确定两种情况
# 当nums【mid】> nums[l]
# 为什么这样比，为不将nums【mid】与target比呢
# 因为nums【mid】> nums[l]时，可以发现nums【l】到nums【mid】为升序
# 若target<numd[mid] and target>nums[l]，则target在mid左边，否则都在右边

# 然后就是 nums【mid】< nums【r】的情况
# 咋样子mid右边都是升序
# 同理，若 target<nums[r] and target>nums[mid]
# target在mid右边（升序序列中），否则都在左边

# 当r<=l的时候，还没找到，就返回

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>=nums[l]: #左边升序
                if target<nums[mid] and target>=nums[l]:
                    r=mid-1
                else:
                    l=mid+1
            elif nums[mid]<=nums[r]:
                if target>nums[mid] and target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        return -1

S=Solution()
print(S.search([4,5,6,7,0,1,2],3))
"""
@File    : 15.三数之和.py
@Time    : 2019-12-09 16:29
@Author  : 李浩然
@Software: PyCharm
@Email: leehaoran@pku.edu.cn
"""


# 类型 数组
# 技巧 双指针

# 思路
# 首先对数组排序
# 首先固定一个数num【i】，将三数之和转化为两数之和
#
# 两数之和使用双指针
# target-=num【i】
# 时间复杂度 on2


from typing import List

class Solution:
    def threeSum(self, nums: List[int],target=0) -> List[List[int]]:
        nums=sorted(nums)
        def two_sum(nums,target):
            ans=[]
            left,right=0,len(nums)-1
            while left<right:
                twosum=nums[left]+nums[right]
                if twosum==target:
                    ans.append([nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while nums[left]==nums[left-1] and left < right: # 避免加入重复元素
                        left+=1
                    while nums[right]==nums[right+1] and right>left:
                        right-=1
                elif twosum<target:
                    left+=1
                else:
                    right-=1



            return ans

        ans=[]
        for i in range(len(nums)-2):
            if nums[i]>target: #第一个元素大于target，退出
                break
            if i>0 and nums[i]==nums[i-1]:
                i+=1
                continue
            ans2=two_sum(nums[i+1:],target-nums[i])
            for a in ans2:
                a.append(nums[i])
                ans.append(a)
        return ans


S=Solution()
nums = [-2,0,1,1,2]
print(S.threeSum(nums))
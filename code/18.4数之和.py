"""
@File    : 18.4数之和.py
@Time    : 2019-11-28 08:44
@Author  : 李浩然
@Software: PyCharm
@Email: 1901210423@pku.edu.cn
"""

from typing import List
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1
        ans = None
        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                if ans is None:
                    ans = []
                ans.append([nums[left], nums[right]])
                left = left + 1
                right = right - 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
                while nums[right] == nums[right + 1] and left < right:
                    right -= 1
            elif target > total:
                left = left + 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
            else:
                right = right - 1
                while nums[right] == nums[right + 1] and left < right:
                    right -= 1
        return ans

    def threeSum(self, nums,target):
        answer = []
        for i in range(len(nums) - 2):
            if nums[i]+nums[i+1]+nums[i+2] > target:  # 最小元素加起来大于target 后面都不行
                break
            if i > 0 and nums[i] == nums[i - 1]:
                i = i + 1  # 跳过重复元素
                continue
            ans = self.twoSum(nums[i + 1:], target - nums[i])
            if ans is not None:
                for a in ans:
                    a.append(nums[i])
                    answer.append(a)
        return answer

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        answer=[]
        for i in range(len(nums)-3):
            if nums[i]+nums[i+1]+nums[i+2]+nums[i+3]>target:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                i = i + 1  # 跳过重复元素
                continue
            ans = self.threeSum(nums[i + 1:], target - nums[i])
            if ans is not None:
                for a in ans:
                    a.append(nums[i])
                    answer.append(a)
        return answer

s=Solution()
nums=[1,-2,-5,-4,-3,3,3,5]

print(s.fourSum(nums,-11))
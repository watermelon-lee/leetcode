# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 如果数组中不存在目标值，返回 [-1, -1]。

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums==[]:
            return [-1,-1]
        ans=[]
        left=self.find_left(nums,target,0,len(nums)-1)
        right=self.find_right(nums,target,0,len(nums)-1)
        if nums[left]==target and nums[right]==target:
            ans.append(left)
            ans.append(right)
        else:
            ans.append(-1)
            ans.append(-1)
        return ans

    def find_left(self,nums,target,left,right):
        while left<right:
            mid = (left + right) // 2
            if nums[mid]==target:
                right=mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return left

    def find_right(self,nums,target,left,right):
        while left<right:
            mid = (left + right) // 2
            if nums[mid]==target:
                if left<right-1:
                    left=mid
                else:
                    return right if nums[right]==target else left
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return right



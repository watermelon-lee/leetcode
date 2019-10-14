# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，
# 使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
#

class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums=sorted(nums)
        diff=100000
        ans=0
        for k,v in enumerate(nums):
            target_now=target-v
            i=k+1
            j=len(nums)-1
            while(i<j):
                if nums[i]+nums[j]>target_now:
                    if (nums[i]+nums[j])-target_now<abs(diff):
                        diff=nums[i]+nums[j]-target_now
                        ans=nums[i]+nums[j]+v
                    j-=1
                else:
                    if  target_now - (nums[i] + nums[j]) < abs(diff):
                        diff = nums[i] + nums[j] - target_now
                        ans = nums[i] + nums[j] + v
                    i+= 1
        return ans


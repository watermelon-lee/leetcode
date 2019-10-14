# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
#
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
#
# 必须原地修改，只允许使用额外常数空间。
#
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pos=0
        flag=0
        if len(nums)==1:
            return nums
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]:
                pos=i-1
                break
            if i==1 and nums[i]<=nums[i-1]:
                flag=1
        if flag==0:
            min=100000
            pos1=pos+1
            for j in range(pos+1,len(nums)):
                if nums[j]>nums[pos] and min>nums[j]:
                    min=nums[j]
                    pos1=j
            temp=nums[pos]
            nums[pos]=nums[pos1]
            nums[pos1]=temp
            nums[pos + 1:] = sorted(nums[pos + 1:])

        else:
            left=0
            right=len(nums)-1
            while right>left:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                right-=1
                left+=1
            #nums=nums[::-1]
        return nums


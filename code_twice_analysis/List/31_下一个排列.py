"""
@File    : 31_下一个排列.py
@Time    : 2019-12-10 14:25
@Author  : 李浩然
@Software: PyCharm
@Email: leehaoran@pku.edu.cn
"""

# 类型 数组
# 技巧 逆向思考

# 我们从最后开始找，找到第一个逆序的二元组（即nums【i】>nums[i-1]）。
# 然后我们在i-1之后的位置，找到比nums【i-1】大，但是最接近的与nums【i-1】交换
# 然后排列nums【i-1】之后的所有元素即可。
# 如 [1,2,3,5,4,3,2,1]
# 我们从后向前遍历首先找到第一个逆序[5,3]，以3所在位置为分界向右找，找到比3大，但是最接近3的交换
# 我们可以找到4这个元素，与3交换之后，[1,2,4,5,3,3,2,1]，这个时候在将4之后的元素升序排序即可，[1,2,4,1,2,3,3,5]
# 若找到最后无逆序二元组，则需要反转整个数组


from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag=0,
        pos=0
        for i in range(len(nums)-1,-1,-1):
            # 找到逆序的话就标记好位置，退出
            if nums[i]>nums[i-1]:
                flag=1
                pos=i-1
                break
        if flag:
            # 从标记位置找到比nums【i-1】大，但是最接近的与nums【i-1】交换
            min_pos=0 # 标记要找的位置
            min_gap=10000 # 标记差值
            for i in range(pos+1,len(nums)):
                if nums[i]>nums[pos] and nums[i]-nums[pos]<min_gap:
                    min_pos=i
                    min_gap=nums[i]
            # 交换pos位置和min_pos位置两个元素
            tmp=nums[pos]
            nums[pos]=nums[min_pos]
            nums[min_pos]=tmp
            nums[pos+1:]=sorted(nums[pos+1:]) #对pos之后的元素排序

        else: #反转数组
            nums=nums[::-1]
        return nums

S=Solution()

nums=[5,4,3,2,1]

print(S.nextPermutation(nums))

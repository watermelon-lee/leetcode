"""
@File    : 75.颜色分类.py
@Time    : 2019-09-23 08:45
@Author  : Wade
@Software: PyCharm
"""

from typing import List
class Solution:
    def sortColors(self, nums: List[int]):
        """
        Do not return anything, modify nums in-place instead.
        """
        count={'red':0,'blue':0,'white':0}
        for i in range(len(nums)):
            if nums[i]==0:
                count['red']+=1
            elif nums[i]==1:
                count['white']+=1
            else:
                count['blue']+=1

        red=int(count['red'])
        white=int(count['red']+count['white'])

        nums[:red]=[0 for i in range(0,red)]
        nums[red:white]=[1 for i in range(red,white)]
        nums[white:]=[2 for i in range(white,len(nums))]
        return nums

s=Solution()
nums=[1,2,0,1,2,0,0,0,2,2,1,1]
print(s.sortColors(nums))
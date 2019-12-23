"""
@File    : 169.多数元素.py
@Time    : 2019-12-23 15:50
@Author  : LEE
@Software: PyCharm
@Email: leehaoran@pku.edu.cn
"""


# 类型 数组

# 思路
# 题目考察数组中的主元素，也就是出现次数大于一半的元素。所以主元素数出现次数-其他所有元素出现次数>0
# 从第一个元素开始，将众数标记为第一个元素，count=1
# 向后遍历，相同count+1，不相同count-1
# 当count为0的时候，就将主元素标记为当前元素，在向后遍历
# 最后count>0的元素被标记着，就是主元素。

# 法二
# 还有可以用哈希表法
# 遍历一遍得到每个元素出现次数，返回哈希表中值最大的键。



from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=1
        main_num=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==main_num:
                count+=1
            else:
                count-=1
            if count==0:
                main_num=nums[i]
                count=1
        return main_num

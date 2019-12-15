"""
@File    : 4.寻找两个有序数组中位数.py
@Time    : 2019-12-09 11:10
@Author  : 李浩然
@Software: PyCharm
@Email: leehaoran@pku.edu.cn
"""

# 类型 数组
# 技巧 递归，二分

# 思路
# 首先要求复杂度是log级别，那么我们每次需要去掉一半的元素
# 找中位数等价于找到第（len1+len2）/2小的数。
# 首先我们保证num2是最长的
# 我们尝试每次去掉k//2个元素
# 比较两个数组k//2-1位置的数字，然后可以去这两个数字较小的数组中左边k//2个数
# 要注意的是，num1比较短，有可能num1比k//2要短，
# 我们对num1最后一个与num2 k//2-1位置的数比较。
# 若num1最后一个小于num2 k/2-1位置的数字，这种时候我们去掉整个num1即可


from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findKth(num1,num2,k):
            if len(num1) > len(num2): #保证num2是长的
                return findKth(num2, num1, k)
            if len(num2)==0:
                return num1[k-1]
            if len(num1)==0:
                return num2[k-1]

            if k==1:
                return min(num1[0],num2[0])



            # 思路是每次去掉k//2个数字

            if k//2>len(num1):
                # 当k//2比num1要长，那么在num1中只能去掉len（num1）个
                if num1[-1]<num2[k//2-1]:
                    # num1可以全部去掉了
                    return findKth([],num2,k-len(num1))
                else:
                    # 从num2中去掉前k//2个，因为他们中不可能有中位数
                    num2=num2[k//2:]
                    return findKth(num1,num2,k-k//2)
            else: #else情况中满足每次都删去k//2
                if num1[k//2-1]>num2[k//2-1]:#删除num2中小的k//2个
                    num2=num2[k//2:]
                else:
                    num1=num1[k//2:]
                return findKth(num1,num2,k-k//2)


        mid1=findKth(nums1,nums2,(len(nums1)+len(nums2)+1)//2)
        mid2=findKth(nums1,nums2,(len(nums1)+len(nums2)+2)//2)

        return (mid2+mid1)/2




S=Solution()
nums1 = [1,2,]
nums2 = [3,4]
print(S.findMedianSortedArrays(nums1,nums2))

"""
@File    : 84.柱状图中最大的矩形.py
@Time    : 2019-11-28 15:13
@Author  : 李浩然
@Software: PyCharm
@Email: 1901210423@pku.edu.cn
"""

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # 双指针，超时
        # max_rec=0
        # for i in range(len(heights)):
        #     square=0
        #     right,left=i,i
        #     for left in range(i,-1,-1):
        #         if heights[left]<heights[i]:
        #             left+=1
        #             break
        #     for right in range(i,len(heights),1):
        #         if heights[right]<heights[i]:
        #             right-=1
        #             break
        #     square=(right-left+1)*heights[i]
        #     if square>max_rec:
        #         max_rec=square
        # return max_rec

        # 考虑优化，当我们找 i 左边第一个小于 heights[i]
        # 如果 heights[i-1] >= heights[i] 其实就是和 heights[i-1] 左边第一个小于 heights[i-1] 一样。
        # 依次类推，右边同理。
        if not heights:
            return 0
        n=len(heights)
        left=[0]*n
        right=[0]*n

        left[0]=0
        right[-1]=n-1


        for i in range(1,n):
            l=i

            for l in range(i-1,-1,-1):
                if heights[l]<heights[i]:
                    l+=1
                    break
            left[i] = l
        for i in range(0,n-1):
            r=i
            for r in range(i+1,n,1):
                if heights[r]<heights[i]:
                    r-=1
                    break
            right[i] = r

        max_rec=0
        for i in range(n):
            max_rec= max((right[i]-left[i]+1)*heights[i],max_rec)
        return max_rec






if __name__=='__main__':
    S=Solution()
    h=[]
    print(S.largestRectangleArea(h))
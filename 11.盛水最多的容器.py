# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 说明：你不能倾斜容器，且 n 的值至少为 2。


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        max = 0
        while j > i:
            if max < min(height[i], height[j]) * (j - i):
                max = min(height[i], height[j]) * (j - i)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max

        # if len(height)==2:
        #     return min(height)
        # max=0
        # for i in range(len(height)):
        #     for j in range(i+1,len(height)):
        #         if(min(height[i],height[j])*(j-i)>max):
        #             max=min(height[i],height[j])*(j-i)
        # return max
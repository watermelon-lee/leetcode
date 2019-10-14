class Solution:
    def trap(self,height):
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        max_left[0] = height[0]
        max_right[-1] = height[-1]
        # 找位置i左边最大值
        for i in range(1, n):
            max_left[i] = max(height[i-1], max_left[i - 1])
        # 找位置i右边最大值
        for i in range(n - 2, -1, -1):
            max_right[i] = max(height[i+1], max_right[i + 1])
        sum=0
        for i in range(n):
            sum += max(0,min(max_left[i], max_right[i]) - height[i])
        return sum



height=[5,4,1,2]
s=Solution()
print(s.trap(height))
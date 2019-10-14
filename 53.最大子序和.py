class Solution:
    def maxSubArray(self,nums):
        sum=0
        max=-1000
        for end in range(0,len(nums)):
            sum+=nums[end]
            if sum>max:
                max=sum
            if sum<0:
                sum=0
        return max

s=Solution()
nums= [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(nums))

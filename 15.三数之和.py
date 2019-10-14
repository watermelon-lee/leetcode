class Solution:
    def threeSum(self, nums):
        answer=[]
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i]>0:  #最小元素大于0 后面都不行
                break
            if i>0 and nums[i]==nums[i-1]:
                i=i+1   # 跳过重复元素
                continue
            ans=self.twoSum(nums[i+1:],0-nums[i])
            if ans is not None:
                for a in ans:
                    a.append(nums[i])
                    answer.append(a)
        return answer





    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left=0
        right=len(nums)-1
        ans=None
        while left<right:
            total=nums[left]+nums[right]
            if total==target:
                if ans is None:
                    ans=[]
                ans.append([nums[left],nums[right]])
                left=left+1
                right=right-1
                while nums[left]==nums[left-1] and left<right:
                    left+=1
                while nums[right] == nums[right + 1] and left < right:
                    right -= 1
            elif target>total:
                left=left+1
                while nums[left]==nums[left-1] and left<right:
                    left+=1
            else:
                right=right-1
                while nums[right] == nums[right + 1] and left < right:
                    right-=1
        return ans






s=Solution()
nums = [-2,0,0,2,2]

print(s.threeSum(nums))






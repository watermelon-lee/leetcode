class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic={}
        ans=[]
        for k,v in enumerate(nums):
            dic[v]=k
        for i in range(len(nums)):
            j=dic.get(target-nums[i])
            if j is not None and i != j:
                ans.append(i)
                ans.append(dic[target-nums[i]])
                return ans
        return

    # def twoSum(self,nums, target):
    #     hashmap = {}
    #     for ind, num in enumerate(nums):
    #         hashmap[num] = ind
    #     for i, num in enumerate(nums):
    #         j = hashmap.get(target - num)
    #         if j is not None and i != j:
    #             return [i, j]



s=Solution()
nums=[3,3]
print(s.twoSum(nums,6))

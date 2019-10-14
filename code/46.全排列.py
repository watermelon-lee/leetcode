class Solution:
    def permute(self, nums):
        nums.sort()
        return self.printSort(nums,ans_now=[],ans=[])



    def printSort(self,nums,ans_now,ans):
        if len(nums)==1:
            ans_now.append(nums[0])
            ans.append(ans_now)
            ans_now=[]
            return ans
        else:
            for i in range(len(nums)):
                new_ans_now=ans_now.copy()
                new_ans_now.append(nums[i])
                new_nums=nums.copy()
                new_nums.remove(nums[i])
                self.printSort(new_nums,new_ans_now.copy(),ans)
        return ans
s=Solution()
nums=[1]
print(s.permute(nums))



ans=[]
class Solution:
    def combinationSum(self, candidates,target):
        nums=[]
        candidates.sort()
        self.find(candidates,target,nums)
        return ans

    # Python 中可变对象是引用传递，因此需要将当前 path 里的值拷贝出来
    # 或者使用 path.copy()

    def find(self,candidates,target,nums):
        if target==0:
            ans.append(nums)
            return
        for i in range(len(candidates)):
            now_target=target-candidates[i]
            if target<0:
                break
            nums.append(candidates[i])
            self.find(candidates[i:],now_target,nums.copy())
            nums.pop() # 元素遍历之后出栈

s=Solution()
candidates=[2,3,6,7]
target=7
print(s.combinationSum(candidates,target))
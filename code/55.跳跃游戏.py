class Solution:
    def canJump(self,nums):
        end=-1
        flag=1
        if len(nums)==1:
            return True
        if nums[0]==0 and len(nums)>1:
            return False
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==0:
                end=i
                flag=0
                break
        distance=1
        arrive=0
        for i in range(end-1,-1,-1):
            if (nums[i]-distance >0 and arrive==0) or (arrive==1 and nums[i]-distance>=0):
                end=i
                flag=1
                distance=1
                arrive=1
            elif nums[i]-distance==0 and end==len(nums)-1:
                end=i
                flag=1
                distance=1
                arrive=1
            else:
                distance+=1
                flag=0
        if flag:
            return True
        else:
            return False

s=Solution()
nums=[3,2,1,0,4]
print(s.canJump(nums))
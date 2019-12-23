"""
@File    : 415.字符串相加.py
@Time    : 2019-12-16 13:02
@Author  : 李浩然
@Software: PyCharm
@Email: leehaoran@pku.edu.cn
"""
# 类型 数学/字符串

# 思路
# 每一位遍历，然后相加，用count表示进位

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # 假设num1长于或者等于num2


        # if len(num2)>len(num1):
        #     tmp=num1
        #     num1=num2
        #     num2=tmp
        #
        # num1 = list(num1)[::-1]
        # num2 = list(num2)[::-1]
        # count = 0
        # j = 0
        # ans=''
        # for j in range(len(num2)):
        #     tmp = int(num1[j]) + int(num2[j]) + count
        #     count = tmp // 10
        #     num = tmp % 10
        #     ans += str(num)
        # j+=1 # 因为在上边循环退出了 j没有+1
        # while count > 0 and j<len(num1):
        #     tmp = int(num1[j]) + count
        #     j += 1
        #     count = tmp // 10
        #     num = tmp%10
        #     ans+=str(num)
        # if count>0:
        #     ans+='1'
        # else:
        #     while j<len(num1):
        #         ans+=num1[j]
        #         j+=1
        # ans=ans[::-1]
        # return ans

        ans=''
        i=0
        count=0
        num1=num1[::-1]
        num2=num2[::-1]
        while i<len(num1) or i<len(num2):
            a=int(num1[i]) if i<len(num1) else 0
            b=int(num2[i]) if i<len(num2) else 0
            tmp=a+b+count
            num=tmp%10
            count=tmp//10
            ans=str(num)+ans
            i+=1
        if count>0:
            ans=str(count)+ans
        return ans


S=Solution()
num1='90301238012'
num2='2137249308401048012898942'
print(int(num1)+int(num2))
print(S.addStrings(num1,num2))
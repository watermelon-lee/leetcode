"""
@File    : 43.字符串相乘.py
@Time    : 2019-12-16 12:38
@Author  : 李浩然
@Software: PyCharm
@Email: leehaoran@pku.edu.cn
"""


# 类型 数学

# 思路
# 大数的乘法，我们可以转换为多个大数的加法
# 我们保存每一位与另一个数乘出来的结果，最后将所有结果相加
# 相加的时候记得在不同位数乘出来的结果在后面补0
# 此外要消除数字开头重复的0 如 00000 变为 0

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        count=0

        ans_list=[]
        for i in range(len(num1)-1,-1,-1):
            count=0
            ans = ''
            for j in range(len(num2)-1,-1,-1):
                tmp=int(num1[i])*int(num2[j])+count
                num=tmp%10 #该位的数
                count=tmp//10 # 进位的数
                ans=str(num)+ans
            if count>0:
                ans= str(count)+ans
            ans_list.append(ans)

        ans='0'
        for i in range(len(ans_list)):
            ans=self.add(ans,ans_list[i]+'0'*i)

         # 除去数字开始重复的0 如 00000 变为0
        while ans[0]=='0' and len(ans)>1:
            ans=ans[1:]
        return ans



    def add(self,num1,num2):
        ans = ''
        i = 0
        count = 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        while i < len(num1) or i < len(num2):
            a = int(num1[i]) if i < len(num1) else 0
            b = int(num2[i]) if i < len(num2) else 0
            tmp = a + b + count
            num = tmp % 10
            count = tmp // 10
            ans = str(num)+ans
            i += 1
        if count > 0:
            ans = str(count)+ans
        return ans

S=Solution()
num1='23123'
num2='0'
print(int(num1)*int(num2))
print(S.multiply(num1,num2))
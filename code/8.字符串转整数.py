"""
@File    : 8.字符串转整数.py
@Time    : 2019-11-25 08:35
@Author  : 李浩然
@Software: PyCharm
@Email: 1901210423@pku.edu.cn
"""


class Solution:
    def myAtoi(self, str) -> int:
        nums='0123456789'
        char='-+'
        ans=[]
        str=str.lstrip()
        for i in range(len(str)):
            if i==0 and str[i] in char:
                ans.append(str[i])
            elif str[i] in nums:
                ans.append(str[i])
            else:
                break
        if len(ans)==0:
            return 0
        elif len(ans)==1 and ans[0] in char:
            return 0
        else:
            number=''
            for i in ans:
                number=number+i
            digit=int(number)
            if digit>pow(2,31)-1:
                return pow(2,31)-1
            elif digit<pow(-2,31):
                return pow(-2,31)
            else:
                return digit


S=Solution()

str="-91283472332 "
print(S.myAtoi(str))
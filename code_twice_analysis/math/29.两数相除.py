"""
@File    : 29.两数相除.py
@Time    : 2019-12-23 08:49
@Author  : LEE
@Software: PyCharm
@Email: leehaoran@pku.edu.cn
"""


# 类型 数学
# 技巧 递归

# 思路
# 对于两个数a,b 要求a/b
# 如果a<b 那么答案是0，即count=0
# 否则，我们设定count=1
# 如果我们每次都用减法，a=a-b,count+=1,这样子效率很低
# 我们每次让b翻倍，即b=b+b，然后与a比大小，如果比a小，就继续翻倍，更新count+=count
# 直到某一次如果翻倍的话，b+b>a，我们停止翻倍过程，让a=a-b，
# 这样问题就可以转化为求 a-b/b0 注意b0是最初的b，也就是最开始的除数，我们在除的过程中改变了b。
# 因此问题递归的化为 count + div(a-b,b0)
# 这样一直递归下去最后到达a<b return 0 就可以结束递归了

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        def div(a,b):
            count=0
            if a>=b:
                count+=1
            else:
                return count
            while a>b:
                if b+b>a:
                    break
                b= (b+b)
                count+=count

            return count+div(a-b,divisor)

        if divisor==1:
            return dividend if dividend<pow(2,31)-1 else pow(2,31)-1
        if divisor==-1:
            return -dividend if -dividend<pow(2,31)-1 else pow(2,31)-1

        sign=1 if dividend>0 and divisor>0 or dividend<0 and divisor<0 else -1
        dividend=abs(dividend)
        divisor=abs(divisor)

        ans=div(dividend,divisor)

        return -ans if sign<0 else ans


S=Solution()

a=-2147483648

b=-1
print(S.divide(a,b))
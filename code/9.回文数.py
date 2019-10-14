#判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False
        y = []
        z = []
        count = 0
        while x != 0:
            y.append(x % 10)
            x = x // 10
        z = y[0:(len(y) + 1) // 2]
        y = y[(len(y) // 2):]
        y = y[::-1]
        return z == y

#         if x<0:
#             return False
#         forward=str(x)
#         backword=str(x)[::-1]
#         if forward==backword:
#             return True
#         return False


s=Solution()
nums = input("input a num")
print(nums)

print(s.isPalindrome(nums))



# 此时可以使用转换，方法有多种：
#
# 1.指定类型转换
#
# 1 >>> y = int(input())
# 2 10
# 3 >>> type(y)
# 4 <class 'int'>
# 2.自动转换
#
# 函数eval() 用来执行一个字符串表达式，并返回表达式的值
#
# eval(expression, globals[ ], locals[ ])
#
# global 和 locals 分别相当于全局和局部变量，eval函数会优先在局部变量存储空间中检索
#
# 1  >>> y = eval(input())
# 2  4.5
# 3  >>> type(y)
# 4 <class 'float'>
# 3.切割转换
#
# 利用函数split()通过指定分隔符对字符串进行切片。
#
# str.split(str="", num=string.count(str))
#
# str为分割符，包括空格、\n，\t 等 ，num是分割次数。
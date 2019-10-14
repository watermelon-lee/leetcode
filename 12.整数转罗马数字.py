# 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        char = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        nums = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        ans = ""
        for i in range(len(nums) - 1, -1, -1):
            while (num >= nums[i]):
                num -= nums[i]
                ans += char[i]
        return ans

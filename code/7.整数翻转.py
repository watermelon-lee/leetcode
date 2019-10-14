#一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

class Solution:
    def reverse(self, x: int) -> int:
        strx = str(x)
        maxNum = 2147483647
        minNum = -2147483648

        y = ""
        if (strx[0] == "-"):
            y += "-"
            strx = strx[1:]

        y += strx[::-1]  # 使用切片

        y = int(y)

        if y > maxNum or y < minNum:
            return 0

        return y
# 实现 strStr() 函数。
#
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ans = 0
        if len(needle) == 0:
            return ans
        else:
            for i in range(len(haystack)):
                ans = i
                count = i
                for j in range(len(needle)):
                    if needle[j] != haystack[count]:
                        break
                    if j == len(needle) - 1:
                        return ans
                    if needle[j] == haystack[count]:
                        count += 1
                        if count == len(haystack):
                            return -1

        return -1


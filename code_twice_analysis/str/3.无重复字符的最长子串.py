"""
@File    : 3.无重复字符的最长子串.py
@Time    : 2019-12-17 12:17
@Author  : 李浩然
@Software: PyCharm
@Email: leehaoran@pku.edu.cn
"""

# 类型 字符串
# 技巧 滑动窗口

# 思路
# 我们只需遍历一遍s
# 使用一个字符串 string（其实最好是字典，但是没想到字典如何去掉重复字符前的串）来记录无重复子串
# i指针向后遍历，若遍历的字符没有出现在string中，则向string中添加，并记录最大长度
# 若i指针在string中出现在了j位置，则将i指针出现的元素添加到string中，并删除j指针以及其指针之前的元素（保持连续）
# 最终遍历完s，我们就可以得到最长的子串值


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length=0
        count=0
        string=''

        for i in range(len(s)):
            if s[i] not in string:
                string+=s[i]
                count+=1
                if count>max_length:
                    max_length=count
            else:
                index = string.index(s[i])
                string+=s[i]
                string=string[index+1:]
                count=len(string)
        return max_length



S=Solution()

s='aab'
print(S.lengthOfLongestSubstring(s))
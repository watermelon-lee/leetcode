"""
@File    : 3.无重复字符的最长子串.py
@Time    : 2019-4-12 14:17
@Author  : 李浩然
@Software: PyCharm
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        count=0
        words=""
        for c in s:
            if c not in words:
                words+=c
                count+=1
            else:
                if count>ans:
                    ans=count
                index=words.index(c)
                words=words[index+1:]+c
                count=len(words)
        if(count>ans):
            ans=count
        return ans
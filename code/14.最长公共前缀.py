# 输入: ["flower","flow","flight"]
# 输出: "fl"
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        ans = ""
        big = max(strs)
        small = min(strs)
        for i in range(min(len(small), len(big))):
            if small[i] != big[i]:
                break
            else:
                ans += big[i]
        return ans

        # if len(strs)==0:
        #     return ""
        # ans=strs[0]
        # for i in range(1, len(strs)):
        #     if len(strs[i])==0:
        #         return ""
        #     for j in range(min(len(strs[i]),len(ans))):
        #         if j==min(len(strs[i]),len(ans))-1 and ans[j] == strs[i][j]:
        #             ans=ans[:j+1]
        #         if ans[j] != strs[i][j]:
        #             ans = ans[:j]
        #             break
        # return ans
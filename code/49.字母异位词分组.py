class Solution:
    def groupAnagrams(self,strs):
        ans=[]
        strs2=strs.copy()
        dic={}
        for i in range(len(strs)):
            list1=list(strs[i])
            list1.sort()
            strs[i]=''.join(list1)
            if strs[i] not in dic:
                dic[strs[i]]=[strs2[i]]
            else:
                dic[strs[i]].append(strs2[i])

        return list(dic.values())


s=Solution()
strs=["eat", "tea", "tan", "ate", "nat", "bat"]
print(s.groupAnagrams(strs))


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        char=["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
        nums=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
        count=0
        ans=0
        for i in range(len(char)-1,-1,-1):
            while count<len(s):
                if len(char[i])==1:
                    if s[count]==char[i]:
                        ans+=nums[i]
                        count+=1
                    else:
                        break
                else:
                    if count<len(s)-1 and s[count]+s[count+1]==char[i]:
                        ans+=nums[i]
                        count+=2
                    else:
                        break
        return ans
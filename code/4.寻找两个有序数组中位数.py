class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # one list is empty

        if len(nums1) > len(nums2):
            nums = nums1
            nums1 = nums2
            nums2 = nums
        mid1=self.findk(nums1,nums2,(len(nums1)+len(nums2)+1)//2)
        mid2=self.findk(nums1,nums2,(len(nums1)+len(nums2)+2)//2)
        return (mid1+mid2)/2

    def findk(self,nums1,nums2,k):
        if len(nums1)>len(nums2):
            return self.findk(nums2,nums1,k)
        if len(nums1)==0:
            return nums2[k-1]
        if k==1:
            return min(nums1[0],nums2[0])
        # if k//2>=len(nums1):
        #     if nums1[len(nums1)-1]<nums2[k//2-1]:
        #         return self.findk([],nums2,k-len(nums1))
        #     else:
        #         nums2=nums2[k//2:]
        #         return self.findk(nums1,nums2,k-k//2)
        # else:
        #     if nums1[k//2-1]<nums2[k//2-1]:
        #         nums1=nums1[k//2:]
        #         return self.findk(nums1,nums2,k-k//2)
        #     else:
        #         nums2=nums2[k//2:]
        #         return self.findk(nums1,nums2,k-k//2)
        k1=min(k//2,len(nums1))
        if nums1[k1 - 1] < nums2[k // 2 - 1]:
            nums1=nums1[k1:]
            return self.findk(nums1,nums2,k-k1)
        else:
            nums2=nums2[k//2:]
            return self.findk(nums1,nums2,k-k//2)



s=Solution()
nums1=[1,2]
nums2=[3,4]
print(s.findMedianSortedArrays(nums1,nums2))
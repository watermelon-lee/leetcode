class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        count = 0

        while (count < len(nums)):
            i = count + 1
            while (i < len(nums) and nums[i] == nums[count]):
                del nums[i]
            count += 1
        return len(nums)


# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

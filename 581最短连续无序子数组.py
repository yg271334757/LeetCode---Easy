class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tem = sorted(nums)
        if tem == nums:
            return 0
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] == tem[l]:
                l += 1
            elif nums[r] == tem[r]:
                r -= 1
            else:
                return r - l + 1
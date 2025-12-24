class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        isRotated=False
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                if not isRotated:
                    isRotated=True
                else:
                    return False
        if isRotated and nums[-1]>nums[0]:
            return False
        return True
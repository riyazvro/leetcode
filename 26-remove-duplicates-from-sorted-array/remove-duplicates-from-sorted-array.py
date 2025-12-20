class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=1
        for i in range(len(nums)):
            if i>0:
                if nums[i]!=nums[i-1]:
                    nums[l]=nums[i]
                    l+=1
    
        numsToPop=len(nums)-l
        while numsToPop>0:
            nums.pop()
            numsToPop-=1
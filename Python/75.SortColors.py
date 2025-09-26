class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = [0,0,0]

        for i,val in enumerate(nums):
            count[val] += 1

        for i in range(0, len(nums)):
            if(count[0]!=0):
                nums[i]=0
                count[0] -= 1
            elif(count[1]!=0):
                nums[i]=1
                count[1] -= 1
            else:
                nums[i] = 2



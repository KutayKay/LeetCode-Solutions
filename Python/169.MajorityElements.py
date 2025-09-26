class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        count = 0
        majority = 0

        for i in range(len(nums)):
            if count == 0 and majority != nums[i]:
                majority = nums[i]
                count += 1
            elif majority == nums[i]:
                count += 1
            else:
                count -= 1

        return majority
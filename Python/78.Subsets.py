class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = []
        n = len(nums)

        def backtrack(op, start_index):
            if start_index == n:
                subsets.append(list(op))
                return

            # include current element
            op.append(nums[start_index])
            backtrack(op, start_index +1)

            op.pop()

            # don't include
            backtrack(op, start_index +1)

        backtrack([], 0)

        return subsets
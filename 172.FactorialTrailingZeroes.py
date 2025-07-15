class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        divisor = 5

        while n >= divisor:
            count += n // divisor
            divisor *= 5

        return count
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        from math import factorial

        numbers = list(range(1, n + 1))
        fact = factorial(n)
        k -= 1  # 0-based indexing
        result = []

        for i in range(n):
            fact //= (n - i)
            index = k // fact
            result.append(str(numbers[index]))
            numbers.pop(index)
            k %= fact

        return ''.join(result)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        r = len(matrix)
        c = len(matrix[0])

        low = 0
        high = (r*c)-1

        while low <= high:
            mid = (low+high)//2
            row, col = divmod(mid, c)

            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                high = mid-1
            else:
                low = mid+1
        return False

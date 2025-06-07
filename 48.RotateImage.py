class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        """
        The rows of the result matrix consists of the elements of columns of the input matrix in reverse order.
        Hence we take each column reverse it and make it the row of the result matrix.
        """
        n = len(matrix)

        "Transpose"
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        "Reverse list and make it the row of the result matrix"
        for row in matrix:
            row.reverse()
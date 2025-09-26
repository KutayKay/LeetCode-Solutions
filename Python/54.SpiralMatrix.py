class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        top, left = 0, 0
        bottom, right = len(matrix)-1, len(matrix[0])-1 
        arr = []

        while top<=bottom and left<=right:
            # Traverse top row 
            for i in range(left, right+1):
                arr.append(matrix[top][i])
            top += 1
            
            # Right column
            for i in range(top, bottom+1):
                arr.append(matrix[i][right])
            right -= 1

            # Bottom row
            if top <= bottom:
                for i in range(right, left-1 , -1):
                    arr.append(matrix[bottom][i])
                bottom -= 1
            
            if left <= right:
                for i in range(bottom, top-1, -1):
                    arr.append(matrix[i][left])
                left += 1

        return arr





        
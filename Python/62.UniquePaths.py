class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Array for number of unique path to index
        # Since we can only move down or right, the first row and column all have 1 unique path
        path = [[1]*n] * m

        # Single traversal 
        for i in range(1,m):
            for j in range(1,n):
                path[i][j] = path[i-1][j] + path[i][j-1]

        return path[-1][-1]


        

        # First row is all 1s since only path is to move right.



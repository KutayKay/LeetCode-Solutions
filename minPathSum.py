class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        "Array of shortest path to each square of the grid"
        arr = [[0] * n for _ in range(m)]
        arr[0][0] = grid[0][0]

        "Initialize trivial sums"
        for i in range(1,m):
            arr[i][0] = arr[i-1][0] + grid[i][0]

        for j in range(1, n):
            arr[0][j] = arr[0][j-1] + grid[0][j]

        "Fill the remainin gspots with smallest choice"
        for i in range(1,m):
            for j in range(1, n):
                arr[i][j] = min(arr[i-1][j], arr[i][j-1]) + grid[i][j]

        "Result is in the last element of the array"
        return arr[m-1][n-1]

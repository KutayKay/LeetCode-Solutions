class Solution(object):
    MOD = 10 ** 9 + 7
    def numberOfPaths(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        self.m = len(grid)
        self.n = len(grid[0])
        self.k = k

        self.dp = [[[-1] * k for _ in range(self.n)] for __ in range(self.m)]
        return self.solve(0, 0, 0, grid)

    def isValid(self, i, j):
        return 0 <= i < self.m and 0<= j < self.n
    
    def solve(self, i, j, s, grid):
        if not self.isValid(i, j):
            return 0
        
        s = (s + grid[i][j]) % self.k

        if i == self.m -1 and j== self.n - 1:
            return 1 if s % self.k == 0 else 0
        
        if self.dp[i][j][s] != -1:
            return self.dp[i][j][s]

        down = self.solve(i+1, j, s, grid)
        right = self.solve(i, j + 1, s, grid)

        self.dp[i][j][s] = (down + right) % self.MOD
        return self.dp[i][j][s]
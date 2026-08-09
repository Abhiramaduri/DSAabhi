class Solution(object):
    def onesMinusZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        row_ones = [0]*m
        col_ones = [0]*n

        for i in range(m):
            for j in range(n):
                if grid[i][j] ==1:
                    row_ones[i] +=1
                    col_ones[j] +=1
        ans = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                row_zeros = n - row_ones[i]
                col_zeros = m - col_ones[j]

                ans[i][j]=(
                    row_ones[i] + col_ones[j] - row_zeros - col_zeros
                )
        return ans
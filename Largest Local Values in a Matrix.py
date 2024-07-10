class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = [[0]*(n-2) for _ in range(n-2)]

        for i in range(n-2):
            for j in range(n-2):
                max_local = 0
                for x in range(i,i+3):
                    for y in range(j,j+3):
                        max_local = max(max_local,grid[x][y])
                maxLocal[i][j] = max_local
        return maxLocal

#Class to determine the minimum operations needed (adding or subtracting x from elements in a grid) to convert a m x n 2D integer grid into a uni-value grid where all elements are equal

class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        m, n = len(grid), len(grid[0])
        A = [grid[r][c] for r in range(m) for c in range(n)]

        rem = A[0] % x
        for v in A:
            if rem != v % x:
                return -1
        
        A.sort()
        mid = A[(m * n) // 2]
        return sum(abs(v - mid)//x for v in A)
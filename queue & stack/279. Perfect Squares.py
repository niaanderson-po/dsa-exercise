#Class to find the minimum number of perfect squares that sum to n using BFS
from collections import deque 

class Solution:

    def numSquares(self, n: int) -> int:
        queue = deque([(n,0)])
        visited = set()
        while queue:
            current_num, step = queue.popleft()

            for i in range(1,current_num+1):
                if i**2 > current_num: break
                if i**2 == current_num:
                    return step+1
                if current_num-i**2 not in visited:
                    visited.add(current_num-i**2)
                    queue.append( (current_num-i**2, step+1) )
        
# Fill each empty room (INF) in a grid with the distance to its nearest gate (0), or leave it as INF if no gate is reachable. Leave the walls (-1) as is.
from collections import deque

class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows = len(rooms)
        columns = len(rooms[0])
        visit = set()
        queue = deque()

        def addRoom(r,c):
            if r < 0 or r == rows or c < 0 or c == columns or (r,c) in visit or rooms[r][c] == -1:
                return
            queue.append([r,c])
            visit.add((r,c))
            
        for r in range(rows):
            for c in range(columns):
                if rooms[r][c] == 0:
                    queue.append([r,c])
                    visit.add((r,c))
        distance = 0
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()

                rooms[r][c] = distance
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r , c - 1)
            distance += 1
        
            

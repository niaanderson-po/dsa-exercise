# Class to find the minimum number of turns required to unlock a 4 digit lock starting from "0000" while avoiding deadends using BFS.
from collections import deque

class Solution:

    def openLock(self, deadends: list[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        queue = deque()
        visit = set(deadends)
        queue.append(["0000", 0])

        def children(lock): 
            results = []
            for i in range(4):
                digit = str((int(lock[i])+1)%10)
                results.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i])-1 + 10)%10)
                results.append(lock[:i] + digit + lock[i+1:])
            return results
                
        
        while queue:
            lock, turn = queue.popleft()
            if lock == target:
                return turn
            for child in children(lock):
                if child not in visit:
                    visit.add(child)
                    queue.append([child, turn+1])
        return -1

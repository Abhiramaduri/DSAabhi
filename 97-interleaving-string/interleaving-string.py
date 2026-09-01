from collections import deque

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        
        if m + n != len(s3):
            return False
        queue = deque([(0, 0)])

        visited = {(0, 0)}
        
        while queue:
            i, j = queue.popleft()

            if i == m and j == n:
                return True
            if i < m and s1[i] == s3[i + j] and (i + 1, j) not in visited:
                visited.add((i + 1, j))
                queue.append((i + 1, j))
            if j < n and s2[j] == s3[i + j] and (i, j + 1) not in visited:
                visited.add((i, j + 1))
                queue.append((i, j + 1))
                
        return False
